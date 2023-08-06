#######################################################################
#
# Copyright (C) 2020-2022 David Palao
# Copyright (C) 2020 David Velázquez
#
# This file is part of PacBio data processing.
#
#  PacBioDataProcessing is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  PacBio data processing is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with PacBioDataProcessing. If not, see <http://www.gnu.org/licenses/>.
#
#######################################################################

"""This module contains the high level functions necessary to run
the 'Single Molecule Analysis' on an input BAM file."""


import logging
from pathlib import Path
import os
from tempfile import TemporaryDirectory
import shutil
import csv
from itertools import tee, chain
import time
from collections import defaultdict, Counter
from collections.abc import Iterable
from typing import Optional
from functools import cached_property

from .bam_utils import (
    split_bam_file_in_molecules, gen_index_single_molecule_bams, join_gffs,
    Molecule, count_subreads_per_molecule, estimate_max_mapping_quality
)
from .bam import BamFile
from .logs import config_logging
from .ui.cl import parse_cl_sm_analysis as parse_cl
from .parameters import SingleMoleculeAnalysisParameters
from .ipd import multi_ipd_summary
from .constants import (
    PBMM2_PREF, BLASR_PREF, PI_SHIFTED_PREF, PI_SHIFTED_VARIANT,
    STRAIGHT_VARIANT, MOLECULES_FILE_SUFFIX, MAPQ_MIN_LINES, MAPQ_MAX_LINES
)
from .errors import high_level_handler, SMAPipelineError, SMAMergeError
from .external import Pbmm2, Blasr, CCS

from .utils import (
    DNASeq, Partition, pishift_back_positions_in_gff, make_partition_prefix,
    try_computations_with_variants_until_done, merge_files,
)
from .filters import cleanup_molecules
from .summary import SummaryReport
from .types import PathOrStr
from .methylation import MethylationReport


MODIFIED_BASE_STR = "modified_base"
MISSING_ALIGNED_CCS_MSG = (
    "The methylation analysis requires aligned CCS files --for all variants--"
    " to proceed. Trying to get them..."
)
MISSING_CCS_MSG = (
    "Aligned CCS file cannot be produced without CCS file. "
    "Trying to produce it..."
)
CCS_FILE_FOUND_AND_COMPUTATION_SKIPPED_MSG = (
    "CCS file '{ccs_filename}' found. Skipping its computation."
)


def create_raw_detections_file(
        gffs: Iterable[PathOrStr],
        detections_filename: PathOrStr,
        modification_types: list[str]):
    """Function in charge of creating the *raw detections* file.
    Starting from a set of .gff files, a csv file (delimiter=","),
    the *raw detections* file, is saved with the following columns:

      - mol id: taken from each gff filename (e.g. 'a.b.c.gff' ->
        mol id: 'b');
      - modtype: column number 3 (idx: 2) of the gffs (feature type)
        (e.g. 'm6A');
      - GATC position: column number 5 (idx: 4) of each gff which
        corresponds to the 'end coordinate of the feature' in the
        GFF3 standard;
      - score of the feature: column number 6 (idx: 5); floating point
        (:ref:`Phred-transformed pvalue <phred-transformed-scores>`
        that a kinetic deviation exists at this position)
      - strand: strand of the feature. It can be +, - with obvious
        meanings. It can also be ? (meaning unknown) or . (for non
        stranded features)

    There are more columns. Although their number is not fixed by
    this function, in practice they are 4 in the case of a
    detected modification. In that case these 4 last columns correspond
    to the values given in the 'attributes' column of the gffs
    (col 9; idx 8). For example, given the following attributes column::

      coverage=134;context=TCA...;IPDRatio=3.91;identificationQv=228

    we would get the following 4 'extra' columns in our *raw detections*
    file::

      134,TCA...,3.91,228

    and this is exactly what happens with the m6A modification type.
    Notice that the value of identificationQV is, again, a
    :ref:`phred transformed probability <phred-transformed-scores>` of
    having a detection. See eq. (8) in [1]

    Parsing: All the lines starting by '#' in the gff files are
    ignored. The format of the gff file is GFF3:
    https://github.com/The-Sequence-Ontology/Specifications/blob/master/gff3.md

    [1]: "Detection and Identification of Base Modifications with Single
    Molecule Real-Time Sequencing Data"
    """
    # wouldn't it be good if before writing, a dictionary is created
    # with the data already written to the file?
    # This would be helpful to avoid double writing lines (see isse #17)
    with open(detections_filename, "a") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=",")
        for gff in gffs:
            molecule = str(gff).split(".")[-2]
            with open(gff) as gff_file:
                for line in gff_file:
                    if line.startswith("#"):
                        continue
                    pieces = line.split()
                    if pieces[2] in modification_types:
                        extra = [_.split("=")[1] for _ in pieces[8].split(";")]
                        new_line = [molecule, pieces[2]] + pieces[4:7] + extra
                        csvwriter.writerow(new_line)
    logging.info(f"Raw detections file '{detections_filename}' created")


def restore_old_run(old_path, new_path):  #
    keep_old = False
    if os.path.isdir(old_path) and os.path.isdir(new_path):
        for fn in os.listdir(old_path):
            try:
                shutil.move(str(old_path/fn), str(new_path))
            except Exception as e:
                logging.error(f"Error moving '{fn}': {e}")
                keep_old = True
    try:
        if not keep_old:
            shutil.rmtree(old_path, ignore_errors=True)
    except Exception as e:
        logging.error(f"Error removing '{old_path}': {e}")


# The next should maybe be absorved by MethylationReport, or in
# bam_utils and logging factored out. (?)
def map_molecules_with_highest_sim_ratio(
        bam_file_name: Optional[PathOrStr]) -> dict[int, Molecule]:
    """Given the path to a bam file, it returns a dictionary, whose
    keys are mol ids (ints) and the values are the corresponding
    Molecules.
    If multiple lines in the given BAM file share the mol id, only
    the first line found with the highest similarity ratio (computed from
    the cigar) is chosen: if multiple lines share the molecule ID and
    the highest similarity ratio (say, 1), ONLY the first one is taken,
    irrespective of other factors.
    """
    mols: dict[int, Molecule] = {}
    bam = BamFile(bam_file_name)
    for line in bam.body:
        mol_id = int(line.molecule_id)
        mol = Molecule(mol_id, bam_file_name, line)
        old_mol = mols.setdefault(mol_id, mol)
        if mol != old_mol:
            oldc = old_mol.cigar
            newc = mol.cigar
            if newc.sim_ratio > oldc.sim_ratio:
                mols[mol_id] = mol
    return mols


def generate_CCS_file(
        ccs: CCS, in_bam: Path, ccs_bam_file: Path) -> Optional[Path]:
    """
    Idempotent computation of the Circular Consensus Sequence (CCS)
    version of the passed in ``in_bam`` file done with passed-in ``ccs``
    object.

    :return: the CCS bam file, if it is there, or ``None`` if if could
             not be computed (yet).
    """
    if ccs_bam_file.exists():
        logging.debug(
            CCS_FILE_FOUND_AND_COMPUTATION_SKIPPED_MSG.format(
                ccs_filename=ccs_bam_file
            )
        )
        result = ccs_bam_file
    else:
        logging.warning(MISSING_CCS_MSG)
        ccs_retcode = ccs(in_bam, ccs_bam_file)
        if ccs_retcode is None:
            result = None
        elif ccs_bam_file.exists():
            result = ccs_bam_file
            if ccs_retcode != 0:
                logging.error(
                    f"Although the file '{ccs_bam_file}' has been generated, "
                    "there was an error."
                )
                logging.error(
                    "It is advisable to check the correctness of the generated"
                    " ccs file."
                )
        else:
            logging.critical(
                f"CCS BAM file '{ccs_bam_file}' could not be produced."
            )
            raise SMAPipelineError(
                "The Single Molecule Analysis cannot proceed without a CCS BAM"
                " file. Aborting."
            )
    return result


class SingleMoleculeAnalysis:
    _VARIANTS = (STRAIGHT_VARIANT, PI_SHIFTED_VARIANT)
    _ALIGNED_GENERIC_NAME = {
        STRAIGHT_VARIANT: "aligned",
        PI_SHIFTED_VARIANT: f"{PI_SHIFTED_PREF} aligned",
    }
    _ALIGNED_FILE_PREFIX = {
        STRAIGHT_VARIANT: "{aligner_pref}",
        PI_SHIFTED_VARIANT: f"{PI_SHIFTED_PREF}.{{aligner_pref}}",
    }

    def __init__(self, parameters):
        self.variants = self._VARIANTS
        self.parameters = parameters
        self.input_bam_file = self.parameters.input_bam_file
        self.CCS_bam_file = self.parameters.CCS_bam_file
        self._create_references()
        aligned_input_bam_file = {
            STRAIGHT_VARIANT: None,
            PI_SHIFTED_VARIANT: None,
        }
        aligned_ccs_bam_file = {
            STRAIGHT_VARIANT: None,
            PI_SHIFTED_VARIANT: None,
        }
        self.aligned_bams = {
            "input": aligned_input_bam_file,
            "ccs": aligned_ccs_bam_file
        }
        self._set_aligner()
        self.ccs = CCS(self.parameters.ccs_path)
        self._ensure_input_bam_aligned()
        # _init_summary requires aligned_bams:
        self._init_summary()
        self._ensure_ccs_bam_aligned()
        self._set_tasks()

    @property
    def CCS_bam_file(self):
        """It produces a Circular Consensus Sequence (CCS) version of
        the input BAM file and returns its name. It uses
        :py:func:`generate_CCS_file` to generate the file.
        """
        try_computations_with_variants_until_done(
            generate_CCS_file, (None,),
            self.ccs, self.input_bam_file, self._CCS_bam_file
        )
        return self._CCS_bam_file

    @CCS_bam_file.setter
    def CCS_bam_file(self, value: Optional[Path]) -> None:
        """Sets the underlying attribute to ``value`` if the given value
        is not ``None``, or constructs a ``Path`` instance from
        ``self.input_bam_file`` prepending ``ccs.`` to the name if the
        given value is ``None``.
        """
        if value is None:
            infilename = Path(self.input_bam_file)
            base = infilename.name
            new_base = "ccs." + base
            value = infilename.parent/new_base
        self._CCS_bam_file = value

    def _create_references(self):
        """[Internal method]
        DNA reference sequences are created here. The 'true' reference must
        exist as fasta beforehand, with its index. A π-shifted reference
        is created from the original one. Its index is also made.

        This method sets two attributes which are, both, mappings with
        two keys ('straight' and 'pi-shifted') and values as follows:

        - reference: the values are DNASeq objects
        - fasta: the values are Path objects

        :meta public:
        """
        straight_path = Path(self.parameters.fasta)
        straight = DNASeq.from_fasta(str(straight_path))
        pi_shifted = straight.pi_shifted()
        pi_shifted_path = straight_path.with_name(
            f"{PI_SHIFTED_PREF}."+straight_path.name)
        pi_shifted.write_fasta(str(pi_shifted_path))
        self.reference = {
            STRAIGHT_VARIANT: straight, PI_SHIFTED_VARIANT: pi_shifted
        }
        self.fasta = {
            STRAIGHT_VARIANT: straight_path,
            PI_SHIFTED_VARIANT: pi_shifted_path
        }

    def _init_summary(self) -> None:
        """[Internal method]
        This method creates an instance of ``SummaryReport`` and sets
        an attribute with it.

        :meta public:
        """
        prefix = ""
        if self.partition.is_proper:
            prefix = str(self.partition)+"."
        self.summary_report = SummaryReport(
            self.input_bam_file,
            self.aligned_bams["input"][STRAIGHT_VARIANT],
            self.reference[STRAIGHT_VARIANT],
            figures_prefix=prefix
        )

    def _set_aligner(self) -> None:
        """[Internal method]
        This method decides what aligner to use, sets an attribute with
        it and sets the prefixes (used in log messages) accordingly.

        :meta public:
        """
        # Refactor hint: move next two to DEFAULT_ values somewhere
        Aligner = Pbmm2
        pref = PBMM2_PREF
        aligner_path = self.parameters.aligner_path
        self.common_aligner_options = {}
        if self.parameters.use_blasr_aligner:
            Aligner = Blasr
            pref = BLASR_PREF
            self.common_aligner_options["nprocs"] = (
                self.parameters.nprocs_blasr
            )
        self.aligner = Aligner(aligner_path)
        for variant in self.variants:
            raw_pref = self._ALIGNED_FILE_PREFIX[variant]
            fpref = raw_pref.format(aligner_pref=pref)
            self._ALIGNED_FILE_PREFIX[variant] = fpref

    def _ensure_input_bam_aligned(self) -> None:
        """[Internal method]
        Main check point for aligned input bam files: this method calls
        whatever is necessary to ensure that the input bam is aligned,
        which means: normal (straight) alignment and π-shifted alignment.

        Warning! The method tries to find a pi-shifted aligned BAM if the
        input is aligned based on whether

        1. a file with suitable filename is found, and
        2. it is aligned.

        :meta public:
        """
        inbam = BamFile(self.input_bam_file)
        if inbam.is_aligned:
            logging.info("The input BAM is aligned")
            input_path = Path(self.input_bam_file)
            input_name = input_path.name
            pi_shifted_name = input_name.replace(
                self._ALIGNED_FILE_PREFIX[STRAIGHT_VARIANT], "", 1)
            pi_shifted_name = (
                self._ALIGNED_FILE_PREFIX[PI_SHIFTED_VARIANT] + pi_shifted_name
            )
            candidate = input_path.with_name(pi_shifted_name)
            self.aligned_bams["input"][PI_SHIFTED_VARIANT] = str(candidate)
            aligned_generic_name = self._ALIGNED_GENERIC_NAME[
                PI_SHIFTED_VARIANT]
            if self._exists_pi_shifted_variant_from_aligned_input():
                logging.info(
                    f"...a possible {aligned_generic_name} version of the "
                    f"input BAM was found: '{candidate}'. It will "
                    "be used."
                )
            else:
                self.aligned_bams["input"][PI_SHIFTED_VARIANT] = None
                logging.info(
                    f"...but no {aligned_generic_name} version of the "
                    "input BAM was found."
                )
                self._disable_pi_shifted_analysis()
            self.aligned_bams["input"][STRAIGHT_VARIANT] = self.input_bam_file
        else:
            logging.info("The input BAM is NOT aligned")
            bam_type = "input"
            try_computations_with_variants_until_done(
                self._align_bam_if_no_candidate_found,
                self.variants, inbam, bam_type
            )

    def _exists_pi_shifted_variant_from_aligned_input(self) -> bool:
        """[Internal method]
        It checks that the expected pi-shifted aligned file exists
        and is an aligned BAM file.

        :meta public:
        """
        # pi_shifted_name = input_name.replace(
        #     self._ALIGNED_FILE_PREFIX["straight"],
        #     self._ALIGNED_FILE_PREFIX["pi-shifted"], 1)
        # pi_shifted_candidate = input_path.with_name(pi_shifted_name)
        # pi_shifted_candidate.exists()
        # BamFile(pi_shifted_candidate)
        pi_shifted_candidate = self.aligned_bams["input"][PI_SHIFTED_VARIANT]
        pi_shifted_path = Path(pi_shifted_candidate)
        pi_shifted_bam = BamFile(pi_shifted_candidate)
        return (pi_shifted_path.exists() and pi_shifted_bam.is_aligned)

    def _disable_pi_shifted_analysis(self) -> None:
        """[Internal method]
        If the pi-shifted analysis cannot be carried out, it is disabled
        with this method.

        :meta public:
        """
        logging.warning("...therefore the pi-shifted analysis is disabled")
        self.variants = (STRAIGHT_VARIANT,)

    def _align_bam_if_no_candidate_found(
            self, inbam: BamFile, bam_type: str,
            variant: str = STRAIGHT_VARIANT
    ) -> Optional[str]:
        """[Internal method]
        Auxiliary method used by ``_ensure_input_bam_aligned`` and by
        ``_ensure_ccs_bam_aligned``. Given a ``bam_type`` (among ``input``
        and ``ccs``) and a ``variant``, an initial BAM file is selected
        and a target aligned BAM filename is constructed.
        The method checks first whether the aligned file is there. If a
        plausible candidate is not found, the initial BAM is aligned
        (``straight`` or ``π-shifted``, depending on the ``variant`` and
        using the proper reference). IF, on the other hand, a candidate is
        found, its computation is skipped.

        If the aligner cannot be run (i.e. calling the aligner returns
        ``None``), ``None`` is returned, meaning that the aligner was not
        called. This can happen when the aligner finds a *sentinel file*
        indicating that the computation is *work in progress*.
        (See :py:meth:`pacbio_data_processing.external.Blasr.__call__` for
        more details on the implementation.)
        This mechanism allows reentrancy.

        :return: the aligned input bam file, if it is there, or None if
                 it could not be computed (yet).

        :meta public:
        """
        # If we want to accept a user provided bam, we need to check it
        # before the next block: in that case the name doesn't need to be
        # constructed! If the name set in self.aligned_bams is None, a
        # proper name must be created; else the name found must be used
        # and it is not necessary to make one.
        aligned_generic_name = self._ALIGNED_GENERIC_NAME[variant]
        alignment_prefix = self._ALIGNED_FILE_PREFIX[variant]
        inbam_path = Path(inbam.bam_file_name)
        aligned_bam_file = inbam_path.with_name(
            alignment_prefix+inbam_path.name
        )
        result = str(aligned_bam_file)
        aligned_bam = BamFile(result)
        aligner_options = self.common_aligner_options.copy()
        if bam_type.lower() == "ccs" and (self.aligner.__class__ == Pbmm2):
            aligner_options["preset"] = "CCS"
        if (aligned_bam_file.exists() and
                aligned_bam.is_plausible_aligned_version_of(inbam)):
            logging.info(
                f"...but a possible {aligned_generic_name} version of the "
                f"{bam_type} BAM was found: '{aligned_bam_file}'. It "
                "will be used."
            )
        else:
            aligner_res = self.aligner(
                in_bamfile=inbam_path,
                fasta=self.fasta[variant],
                out_bamfile=aligned_bam_file,
                **aligner_options,
            )
            if aligner_res is None:
                result = None
            else:
                logging.info(
                    f"...since no {aligned_generic_name} version of the "
                    f"{bam_type} BAM was found, one has been produced and it "
                    f"will be used: '{aligned_bam_file}'"
                )
        self.aligned_bams[bam_type][variant] = result
        return result

    def _ensure_ccs_bam_aligned(self) -> None:
        """[Internal method]
        As its name suggests, it is ensured that the aligned variants of
        the CCS file exist.
        The summary report is informed about the aligned CCS files.

        .. note::

           The CCS BAM file is created *before* checking if its aligned
           variants are present. It might seem a logic error to proceed
           this way instead of checking *first* for the existence of
           the aligned variants of the CCS BAM before deciding if the
           computation of the CCS BAM file is needed, but it is not an
           error: in order to decide if a given file can be an aligned
           version of the CCS BAM, we need the CCS BAM itself.

        :meta public:
        """
        logging.info(MISSING_ALIGNED_CCS_MSG)
        ccs_bam = BamFile(self.CCS_bam_file)
        try_computations_with_variants_until_done(
            self._align_bam_if_no_candidate_found, self.variants,
            ccs_bam, "ccs"
        )
        self.summary_report.aligned_ccs_bam_files = self.aligned_bams["ccs"]

    @cached_property
    def partition(self) -> Partition:
        """The target ``Partition`` of the input BAM file that must be
        processed by the current analysis, according to the input
        provided by the user.
        """
        return Partition(
            self.parameters.partition,
            BamFile(self.input_bam_file)
        )

    def _set_tasks(self) -> None:
        opmr = self.parameters.only_produce_methylation_report
        self._do_split_bam = True
        self._do_filter_molecules = True
        self._do_collect_statistics = True
        self._do_generate_indices = not opmr
        self._do_ipd_analysis = not opmr
        self._do_create_raw_detections_file = not opmr
        self._do_produce_methylation_report = True

    def _select_molecules(self) -> None:
        """[Internal method]
        This method is part of the main sequence irrespective of whether
        the user selects to only produce the methylation report, or the
        full analysis.
        After this method the mapping ``_molecules_todo`` is created
        of type dict[int, Molecule], with molecules that:

        1. Belong to the partition,
        2. Are correctly mapped in the aligned CCS file, and
        3. If they belong to the ``pi-shifted`` variant (molecules
           obtained after aligning with a pi-shifted reference) then
           they cross the origin.

        :meta public:
        """
        self._molecule_ids_todo = {}
        for variant in self.variants:
            bam = BamFile(self.aligned_bams["input"][variant])
            mols = {m for m in bam.all_molecules if m in self.partition}
            self._molecule_ids_todo[variant] = mols
        molecules_from_ccs = self._collect_suitable_molecules_from_ccs()
        molecules_from_ccs = (
            self._keep_only_pishifted_molecules_crossing_origin(
                molecules_from_ccs)
        )
        self._crosscheck_molecules_in_partition_with_ccs(molecules_from_ccs)

    # Smell: too many responsabilities!
    def _collect_suitable_molecules_from_ccs(self) -> dict[int, Molecule]:
        """[Internal method]
        Auxiliary routine of _select_molecules in charge of choosing
        *suitable molecules* from the aligned CCS bam files.
        The resulting mapping contains all *suitable molecules* in the
        'straight' variant and the *suitable molecules* in the
        'π-shifted' variant that are *not in* the 'straight' variant.
        The molecules corresponding to both variants will be joined.
        Among all the possible subreads of each molecule in the aligned
        CCS, one is chosen by ``map_molecules_with_highest_sim_ratio``.
        The choice of *suitable molecules* is done by the method
        ``_discard_molecules_with_seq_mismatch``.
        Moreover the molecules are labeled with the variant they belong
        to. It is necessary to do this labeling, so that
        we can later trace what reference each molecule is attached to.

        :meta public:
        """
        _ccs_mols = {}
        for variant in self.variants:
            name = self._ALIGNED_GENERIC_NAME[variant]
            logging.info(f"Generating molecules mapping from {name} CCS file")
            _ccs_mols[variant] = map_molecules_with_highest_sim_ratio(
                self.aligned_bams["ccs"][variant])
            num_mols = len(_ccs_mols[variant])
            for mol in _ccs_mols[variant].values():
                mol.variant = variant
                mol.reference = self.reference[variant]
            logging.debug(f"ccs lines ({name}): {num_mols} molecules found")
        molecules_from_ccs = {}
        for variant in self.variants[::-1]:
            molecules_from_ccs |= self._discard_molecules_with_seq_mismatch(
                _ccs_mols[variant]
            )
        self._report_discarded_molecules_with_seq_mismatch(
            _ccs_mols, molecules_from_ccs
        )
        return molecules_from_ccs

    def _report_discarded_molecules_with_seq_mismatch(
            self,
            mols_in_raw_ccs_files: dict[str, dict[int, Molecule]],
            molecules_from_ccs: dict[int, Molecule]
            ) -> None:
        """[Internal method]
        This method simply logs the ids of discarded molecules and passes
        the infos to the ``SummaryReport`` instance.

        :meta public:
        """
        before_mols = set()
        for variant in self.variants:
            before_mols |= set(mols_in_raw_ccs_files[variant].keys())
        discarded_mols = (before_mols - set(molecules_from_ccs.keys()))
        for mol_id in discarded_mols:
            logging.info(
                f"Molecule {mol_id} discarded due to DNA "
                "sequence mismatch with reference"
            )
        self.summary_report.mols_used_in_aligned_ccs = before_mols
        self.summary_report.mols_dna_mismatches = discarded_mols

    def _discard_molecules_with_seq_mismatch(
            self, molecules_from_ccs: dict[int, Molecule]
            ) -> dict[int, Molecule]:
        """[Internal method]
        The aligned CCS molecules are filtered in this method to keep
        only molecules that match perfectly the corresponding reference
        (ie, taking into account variants).

        :meta public:
        """
        filtered_mols_in_ccs = {}
        for mol_id, mol in molecules_from_ccs.items():
            start = mol.start
            dna_in_ref = self.reference[mol.variant][start:start+len(mol)]
            if dna_in_ref == mol.dna:
                filtered_mols_in_ccs[mol_id] = mol
        return filtered_mols_in_ccs

    def _keep_only_pishifted_molecules_crossing_origin(
            self, molecules_from_ccs: dict[int, Molecule]
            ) -> dict[int, Molecule]:
        """[Internal method]
        This method filters out molecules from the CCS aligned list that
        1. Belong to the π-shifted variant, and
        2. Do not cross the origin
        These molecules are unwanted because the point of including
        π-shifting in the analysis is to catch molecules crossing the
        origin.

        :meta public:
        """
        result = {}
        for mol_id, mol in molecules_from_ccs.items():
            if mol.variant == PI_SHIFTED_VARIANT:
                if not mol.is_crossing_origin(ori_pi_shifted=True):
                    continue
            result[mol_id] = mol
        return result

    def _crosscheck_molecules_in_partition_with_ccs(
            self, molecules_from_ccs: dict[int, Molecule]) -> None:
        """[Internal method]
        This method ensures that only the molecules in the current
        partition are processed. It does it by crosschecking the
        sets corresponding to the partition (for all variants) with
        the set of valid molecules in the ccs file.
        The attribute ``_molecules_todo`` is set, and its type is:

        .. code-block::

            dict[int, Molecule]

        :meta public:
        """
        mol_ids_in_ccs = set(molecules_from_ccs.keys())
        todo = set()
        for variant in self.variants:
            todo = todo.union(
                {int(_) for _ in self._molecule_ids_todo[variant]}
            )
        crosschecked_molecules = mol_ids_in_ccs & todo
        self._molecules_todo = {
            k: molecules_from_ccs[k] for k in crosschecked_molecules
        }

    def _split_bam(self) -> None:
        """[Internal method]
        Produces a generator with 2-tuples of the type
        (mol_id[int], Molecule)
        where the Molecule is related to a single molecule BAM file that
        has been generated by ``split_bam_file_in_molecules``.
        It sets an attribute called ``_per_molecule_bam_generator`` that
        refers to that generator.

        :meta public:
        """
        if self._do_split_bam:
            variants_gens = []
            for variant in self.variants:
                splitted_mols_gen = split_bam_file_in_molecules(
                    self.aligned_bams["input"][variant], self.workdir.name,
                    {id_: mol for id_, mol in self._molecules_todo.items()
                        if mol.variant == variant}
                )
                variants_gens.append(splitted_mols_gen)
            self._per_molecule_bam_generator = chain(*variants_gens)
        else:
            self._per_molecule_bam_generator = ()

    @cached_property
    def _minimum_mapping_quality(self) -> int:
        """[Internal property]
        This attribute (cached, but not intented to be manually
        overwritten) returns the minimum value of the mapping
        quality that is acceptable for the current analysis.
        If a mapping quality threshold is provided in the command line,
        it is used and returned as the attribute value. Otherwise a value
        is computed using the
        py:func:`bam_utils.estimate_max_mapping_quality` function.

        :meta public:
        """
        if self.parameters.mapping_quality_threshold:
            min_mapq = self.parameters.mapping_quality_threshold
        else:
            estimated_max_mapq = estimate_max_mapping_quality(
                BamFile(self.aligned_bams["input"][STRAIGHT_VARIANT]),
                min_lines=MAPQ_MIN_LINES, max_lines=MAPQ_MAX_LINES
            )
            min_mapq = estimated_max_mapq//2
        return min_mapq

    def _filter_molecules(self) -> None:
        """[Internal method]
        The ``_molecules_todo`` mapping is here reduced by removing
        molecules that do not fulfill a minimum requirement of quality.
        The summary report is updated accordingly.
        See the ``cleanup_molecules`` auxiliary function for details
        on the filtering process.
        An attribute called ``_filtered_molecules_generator`` is set
        which produces ``MoleculeWorkUnit`` s.

        :meta public:
        """
        all_molecules_generator = self._per_molecule_bam_generator
        initial_mols = set(self._molecules_todo.keys())
        if self._do_filter_molecules:
            logging.info(
                "[filter] Sieving molecules from input BAM before the "
                "IPD analysis"
            )
            min_mapq = self._minimum_mapping_quality
            logging.debug(
                f"[filter] minimum mapping quality: {min_mapq}"
            )
            clean_molecules = cleanup_molecules(
                all_molecules_generator, min_mapq_cutoff=min_mapq
            )
            clean_molecules, clean_molecules_cp = tee(clean_molecules, 2)
            clean_molecules_redux = {_[0] for _ in clean_molecules}
            self._molecules_todo = {
                k: self._molecules_todo[k] for k in clean_molecules_redux
            }
            self._filtered_molecules_generator = clean_molecules_cp
            filtered_out_mols = initial_mols-set(self._molecules_todo.keys())
        else:
            self._filtered_molecules_generator = all_molecules_generator
            filtered_out_mols = set()
        self.summary_report.filtered_out_mols = filtered_out_mols

    def _collect_statistics(self) -> None:
        """[Internal method]
        It sets an attribute: 'filtered_bam_statistics' that contains
        some data to be consumed by the MethylationReport.
        For now the only data is the number of subreads per molecule
        and per strand.

        :meta public:
        """
        subreads = defaultdict(Counter)
        if self._do_collect_statistics:
            filtered_bams, backup = tee(self._filtered_molecules_generator, 2)
            for (mol_id, molecule) in filtered_bams:
                bam = BamFile(molecule.src_bam_path)
                new = count_subreads_per_molecule(bam)
                for mol, counter in new.items():
                    subreads[mol].update(counter)
            self._filtered_molecules_generator = backup
        self.filtered_bam_statistics = {"subreads": subreads}

    def _generate_indices(self) -> None:
        """[Internal method]
        Indices are generated for all files that need to be analyzed by
        ipdSummary.

        :meta public:
        """
        if self._do_generate_indices:
            self._indexed_molecules_generator = gen_index_single_molecule_bams(
                self._filtered_molecules_generator,
                self.parameters.pbindex_path
            )

    def _ipd_analysis(self) -> None:
        """[Internal method]
        Performs the IPD analysis of the single molecule files.
        Sets a generator with Paths to produced GFF files.

        :meta public:
        """
        if self._do_ipd_analysis:
            self._ipd_processed_molecules = multi_ipd_summary(
                self._indexed_molecules_generator,
                self.parameters.fasta,
                self.parameters.ipdsummary_path,
                self.parameters.num_simultaneous_ipdsummarys,
                self.parameters.num_workers_per_ipdsummary,
                self.parameters.modification_types,
                self.parameters.ipd_model
            )

    def produce_methylation_report(self) -> None:
        params = self.parameters
        mr = MethylationReport(
            detections_csv=params.raw_detections_filename,
            molecules=self._molecules_todo,
            modification_types=params.modification_types,
            filtered_bam_statistics=self.filtered_bam_statistics,
        )
        mr.save()
        self.summary_report.methylation_report = mr.csv_name
        #  Move the next line to MethylationReport.save
        logging.info(f"{mr.PRELOG} Results saved to file '{mr.csv_name}'")

    def _fix_positions(self) -> None:
        """[Internal method]
        The purpose is to shift back the shifted positions in the
        π-shifted molecules.
        Two operations are required to complete that task:

        1. fixing positions in the gff files, and
        2. fixing positions in the molecules themselves.

        :meta public:
        """
        self._fix_positions_in_gffs()
        self._fix_positions_in_molecules()

    def _fix_positions_in_gffs(self) -> None:
        """[Internal method]
        In the case that some molecules have been processed, the
        positions in the gff files corresponding to molecules that have
        been *π-shifted* are shifted back.

        :meta public:
        """
        try:
            ipd_processed_mols = self._ipd_processed_molecules
        except AttributeError:
            return
        self._ipd_processed_molecules, branch = tee(ipd_processed_mols, 2)
        for workunit in branch:
            mol_id, molecule = workunit
            if molecule.variant == PI_SHIFTED_VARIANT:
                gff_path = molecule.gff_path
                if gff_path is not None:
                    pishift_back_positions_in_gff(gff_path)

    def _fix_positions_in_molecules(self) -> None:
        """[Internal method]
        All positions of *π-shifted* molecules are shifted back in the
        ``_molecules_todo`` dictionary (which will be used to generate
        the methylation report).

        :meta public:
        """
        for mol_id, molecule in self._molecules_todo.items():
            if molecule.variant == PI_SHIFTED_VARIANT:
                molecule.pi_shift_back()

    def _report_faulty_molecules(self) -> None:
        """[Internal method]
        The molecules that had any problem in their processing are
        passed to the ``SummaryReport`` as a set.

        :meta public:
        """
        faulty_molecules = set()
        for mol_id, molecule in self._molecules_todo.items():
            if molecule.had_processing_problems:
                faulty_molecules.add(mol_id)
        self.summary_report.faulty_mols = faulty_molecules

    def _dump_results(self) -> None:
        """[Internal method]
        All the output generated is driven by this method:

        * a joint gff file
        * a *per detection* csv file
        * a methylation report
        * a summary report
        * the molecules sets (see
          :py:class:pacbio_data_processing.summary.SummaryReport)

        :meta public:
        """
        if self._do_create_raw_detections_file:
            joint_gffs = join_gffs(
                self._ipd_processed_molecules,
                self.parameters.joint_gff_filename
            )
            create_raw_detections_file(
                joint_gffs,
                self.parameters.raw_detections_filename,
                self.parameters.modification_types,
            )
        self.summary_report.gff_result = self.parameters.joint_gff_filename
        self.summary_report.raw_detections = (
            self.parameters.raw_detections_filename)
        self.summary_report.mapping_quality_threshold = (
            self._minimum_mapping_quality)
        if self._do_produce_methylation_report:
            self.produce_methylation_report()
        self.summary_report.save(
            self.parameters.summary_report_html_filename
        )
        # ##
        # dumping molecules in all cases can seem sloppy, since
        # it is only used to merge partitions (for now). But serves
        # as a preparation step for future optimizations (runs where
        # not the full analysis must be produced):
        # ##                                         (DPalao, 29sep2022)
        self.molecule_sets_filename = (
            self.parameters.summary_report_html_filename.with_suffix(
                MOLECULES_FILE_SUFFIX
            )
        )
        self.summary_report.dump_molecule_sets(self.molecule_sets_filename)

    def _merge_joint_gffs(self) -> None:
        num_parts = self.partition.num_partitions
        current_prefix = make_partition_prefix(
            self.partition.current, num_parts)
        current = self.parameters.joint_gff_filename
        all_ = []
        for ipart in range(1, num_parts+1):
            pref = make_partition_prefix(ipart, num_parts)
            name = current.name.replace(current_prefix, pref, 1)
            filename = current.with_name(name)
            all_.append(filename)
        joint = current.with_name(
            current.name.replace(current_prefix+".", "")
        )
        merge_files(all_, joint)
        self.joint_gffs_filename = joint

    def _merge_raw_detections(self) -> None:
        num_parts = self.partition.num_partitions
        current_prefix = make_partition_prefix(
            self.partition.current, num_parts)
        current = self.parameters.raw_detections_filename
        all_ = []
        for ipart in range(1, num_parts+1):
            pref = make_partition_prefix(ipart, num_parts)
            name = current.name.replace(current_prefix, pref, 1)
            filename = current.with_name(name)
            all_.append(filename)
        joint = current.with_name(
            current.name.replace(current_prefix+".", "")
        )
        merge_files(all_, joint)
        self.joint_raw_detections_filename = joint

    def _merge_methylation_reports(self) -> None:
        num_parts = self.partition.num_partitions
        current_prefix = make_partition_prefix(
            self.partition.current, num_parts)
        _current = self.parameters.raw_detections_filename
        current = _current.with_name("methylation."+_current.name)
        all_ = []
        for ipart in range(1, num_parts+1):
            pref = make_partition_prefix(ipart, num_parts)
            name = current.name.replace(current_prefix, pref, 1)
            filename = current.with_name(name)
            all_.append(filename)
        joint = current.with_name(
            current.name.replace(current_prefix+".", "")
        )
        merge_files(all_, joint, keep_only_first_header=True)
        self.joint_methylation_report_filename = joint

    def _merge_summary_reports(self) -> None:
        sr = SummaryReport(
            self.input_bam_file,
            self.aligned_bams["input"][STRAIGHT_VARIANT],
            self.reference[STRAIGHT_VARIANT]
        )
        sr.methylation_report = self.joint_methylation_report_filename
        sr.raw_detections = self.joint_raw_detections_filename
        sr.gff_result = self.joint_gffs_filename
        sr.aligned_ccs_bam_files = self.aligned_bams["ccs"]
        sr.mapping_quality_threshold = self._minimum_mapping_quality
        num_parts = self.partition.num_partitions
        current_prefix = make_partition_prefix(
            self.partition.current, num_parts)
        current = self.molecule_sets_filename
        for ipart in range(1, num_parts+1):
            pref = make_partition_prefix(ipart, num_parts)
            name = current.name.replace(current_prefix, pref, 1)
            filename = current.with_name(name)
            sr.load_molecule_sets(filename)
        current_html = self.parameters.summary_report_html_filename
        joint = current_html.with_name(
            current_html.name.replace(current_prefix+".", "")
        )
        sr.save(joint)

    @property
    def all_partition_done_filenames(self) -> list[Path]:
        """Attribute that return a list of ``Path``s corresponding
        to the files expected to be found when all the partitions
        are processed (in case of partitioning the input BAM).
        """
        num_parts = self.partition.num_partitions
        current_prefix = make_partition_prefix(
            self.partition.current, num_parts)
        current_done = self.parameters.partition_done_filename
        ready = []
        for ipart in range(1, num_parts+1):
            pref = make_partition_prefix(ipart, num_parts)
            name = current_done.name.replace(current_prefix, pref, 1)
            part_done_filename = current_done.with_name(name)
            ready.append(part_done_filename)
        return ready

    @property
    def all_partitions_ready(self) -> bool:
        """Attribute that answers the question: are all the partitions
        ready?
        """
        return all([_.exists() for _ in self.all_partition_done_filenames])

    def _remove_partition_done_files(self):
        """[Internal method]
        Remove the partition done marker files after the partitions have
        been successfully merged.

        .. warning::

           It is assumed that this is called within the
           :py:meth:_post_process_partition phase.

        :meta public:
        """
        for done_file in self.all_partition_done_filenames:
            done_file.unlink(missing_ok=True)

    def _merge_partitions_if_needed(self) -> None:
        """[Internal method]
        This method merges properly the output files produced during
        the processing of all the partitions, *if* they are ready.

        .. warning::

           It is assumed that this is called within the
           :py:meth:_post_process_partition phase.

        :meta public:
        """
        if self.all_partitions_ready:
            errors = []
            for meth in (
                    self._merge_joint_gffs,
                    self._merge_raw_detections,
                    self._merge_methylation_reports,
                    self._merge_summary_reports,
            ):
                try:
                    meth()
                except Exception as e:
                    errors.append(e)
            if errors:
                msg = "\n"+"\n   ".join(
                    [f"[error #{i}] {_}" for i, _ in enumerate(errors)]
                )
                raise SMAMergeError(msg)
            else:
                self._remove_partition_done_files()

    def _post_process_partition(self) -> None:
        """[Internal method]
        After the analysis is done, if only a fraction (aka ``partition``)
        was processed, this method declares that the analysis of the
        current``partition`` is complete and tries to merge the partitions
        (which will only occur if the proper conditions are met).

        :meta public:
        """
        if self.partition.is_proper:
            Path(self.parameters.partition_done_filename).touch(exist_ok=True)
            try:
                self._merge_partitions_if_needed()
            except SMAMergeError as e:
                logging.error(str(e))

    def _backup_temp_dir_if_needed(self) -> None:
        if self.parameters.keep_temp_dir:
            suffix = ".backup"
            if self.partition.is_proper:
                suffix = "-"+str(self.partition)+suffix
            backup = Path(self.workdir.name+suffix)
            shutil.copytree(Path(self.workdir.name), backup)
            logging.debug(f"Copied temporary dir to: '{backup}'")

    @property
    def workdir(self) -> TemporaryDirectory:
        """This attribute returns the necessary temporary working
        directory on demand and it ensures that only one temporary
        dir is created by caching.
        """
        try:
            wdir = self._workdir
        except AttributeError:
            wdir = TemporaryDirectory(dir=".")
            self._workdir = wdir
        return wdir

    # [G30]: Functions Should Do One Thing
    # [G31]: Hidden Temporal Couplings
    def __call__(self) -> None:
        """Main entry point to perform a single molecule analysis:
        this method triggers the analysis.
        """
        start = time.time()
        self._select_molecules()
        self._split_bam()
        self._filter_molecules()
        self._collect_statistics()
        self._generate_indices()
        self._ipd_analysis()
        self._fix_positions()
        self._report_faulty_molecules()
        self._dump_results()
        self._post_process_partition()
        self._backup_temp_dir_if_needed()
        end = time.time()
        t = end-start
        t_h = t/3600
        logging.info(
            f"Execution time (wall clock time): {t:.2f} s = {t_h:.2f} h")


def _main(config) -> None:
    """This function drives the Single Molecule Analysis once the
    input has been parsed.

    :meta public:
    """
    config_logging(config.verbose)
    params = SingleMoleculeAnalysisParameters(config)
    logging.info(str(params))
    sma = SingleMoleculeAnalysis(params)
    sma()


@high_level_handler
def main_cl() -> None:
    """Entry point for ``sm-analysis`` executable."""
    config = parse_cl()
    _main(config)
