#######################################################################
#
# Copyright (C) 2021, 2022 David Palao
#
# This file is part of PacBioDataProcessing.
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

from pathlib import Path

from ..constants import (
    DEFAULT_ALIGNER_PROGRAM, DEFAULT_PBINDEX_PROGRAM, DEFAULT_IPDSUMMARY_PROGRAM,
    DEFAULT_NUM_SIMULTANEOUS_IPDSUMMARYS, DEFAULT_NUM_WORKERS_PER_IPDSUMMARY,
    DEFAULT_NUM_WORKERS_BLASR, DEFAULT_MODIFICATION_TYPE,
    DEFAULT_DNA_LEN_TH, DEFAULT_NUM_MOL_TH, DEFAULT_QUAL_TH,
    DEFAULT_MINIMUM_MAPPING_RATIO, DEFAULT_CCS_PROGRAM,
)
from .. import __version__


BAM_FILE_METAVAR = "BAM-FILE"
INPUT_BAM_FILE_HELP = "input file in BAM format"
ALIGNMENT_FILE_METAVAR = "ALIGNMENT-FILE"
FASTA_FILE_HELP = (
    "input file containing the alignment in FASTA format (typically "
    "a file ending in '.fa' or '.fasta'). A companion '.fa.fai'/"
    "'.fasta.fai' file is also needed but it will be created if not "
    "found."
)
INPUT_BAM_FILE_4FILTER_HELP = INPUT_BAM_FILE_HELP + (
    ". The output will be another"
    " %(metavar)s with the same name but prefixed with 'parsed.'"
)


# Options for sm-analysis:
# Refactor hint: replace options by instances of custom dataclasses.

_INPUT_BAM_FILE = (
    ("input_bam_file",),
    dict(metavar=BAM_FILE_METAVAR, type=Path, help=INPUT_BAM_FILE_HELP)
)

_FASTA = (
    ("fasta",),
    dict(
        metavar=ALIGNMENT_FILE_METAVAR,
        type=Path,
        help=FASTA_FILE_HELP
    )
)

_IPD_MODEL = (
    ("-M", "--ipd-model"),
    dict(
        type=Path,
        metavar="MODEL",
        help=(
            "model to be used by ipdSummary to identify the type of "
            "modification. MODEL must be either the model name or the "
            "path to the ipd model. "
            "First, the program will make an attempt "
            "to interprete MODEL as a path to a file defining a model; "
            "if that fails, MODEL will be understood to be "
            "the name of a model that must be "
            "accessible in the resources directory of kineticsTools "
            "(e.g. '-M SP3-C3' would trigger a "
            "search for a file called 'SP3-C3.npz.gz' within the "
            "directory with models provided by kineticsTools). "
            "If this option is not given, the default model in "
            "ipdSummary is used."
        )
    )
)

_ALIGNER_PROGRAM = (
    ("-a", "--aligner"),
    dict(
        metavar="PROGRAM",
        default=DEFAULT_ALIGNER_PROGRAM,
        type=Path,
        dest="aligner_path",
        help=(
            "program to use as aligner. It can be a path or an executable "
            "in the PATH (default: '%(default)s')"
        )
    )
)

_PBINDEX_PROGRAM = (
    ("-p", "--pbindex"),
    dict(
        metavar="PROGRAM",
        default=DEFAULT_PBINDEX_PROGRAM,
        type=Path,
        dest="pbindex_path",
        help=(
            "program to generate indices of BAM files. It must have the "
            "same interface as PacBio's 'pbindex' and it can be a path or an "
            "executable in the PATH (default: '%(default)s')"
        )
    )
)

_IPDSUMMARY_PROGRAM = (
    ("-i", "--ipdsummary"),
    dict(
        metavar="PROGRAM",
        default=DEFAULT_IPDSUMMARY_PROGRAM,
        type=Path,
        dest="ipdsummary_path",
        help=(
            "program to analyze the IPDs. It must have the same interface as "
            "PacBio's 'ipdSummary'. It can be a path or an executable in the "
            "PATH (default: '%(default)s')"
        )
    )
)

_CCS_PROGRAM = (
    ("-c", "--ccs"),
    dict(
        metavar="PROGRAM",
        default=DEFAULT_CCS_PROGRAM,
        type=Path,
        dest="ccs_path",
        help=(
            "program to compute the Hi-Fi version of the input BAM. It must "
            "have the same interface as PacBio's 'CCS'. It can be a path or "
            "an executable in the PATH (default: '%(default)s')"
        )
    )
)

_NUM_SIMULTANEOUS_IPDSUMMARYS = (
    ("-N", "--num-simultaneous-ipdsummarys"),
    dict(
        type=int,
        default=DEFAULT_NUM_SIMULTANEOUS_IPDSUMMARYS,
        metavar="NUM",
        help=(
            "number of simultaneous instances of ipdSummary that will "
            "cooperate to process the molecules (default: %(default)s)"
        )
    )
)

_NUM_WORKERS_PER_IPDSUMMARY = (
    ("-n", "--num-workers-per-ipdsummary"),
    dict(
        type=int,
        default=DEFAULT_NUM_WORKERS_PER_IPDSUMMARY,
        metavar="NUM",
        help=(
            "number of worker processes that each instance of ipdSummary will"
            " spawn (default: %(default)s)"
        )
    )
)

_NPROCS_BLASR = (
    ("--nprocs-blasr",),
    dict(
        type=int,
        default=DEFAULT_NUM_WORKERS_BLASR,
        metavar="NUM",
        help=(
            "number of worker processes that each instance of blasr will "
            "spawn (default: %(default)s)"
        )
    )
)

_PARTITION = (
    ("-P", "--partition"),
    dict(
        metavar="PARTITION:NUMBER-OF-PARTITIONS",
        help=(
            "this option instructs the program to only analyze a fraction "
            "(partition) of the molecules present in the input bam file. The "
            "file is divided in `NUMBER OF PARTITIONS` (almost) equal pieces "
            "but ONLY the PARTITION-th partition (fraction) is analyzed. "
            "For instance, `--partition 3:7` means that the bam file is "
            "divided in seven pieces but only the third piece is analyzed "
            "by the current instance of sm-analysis. By default, all the file"
            " is analyzed."
        )
    )
)

_CCS_BAM_FILE = (
    ("-C", "--CCS-bam-file"),
    dict(
        metavar="BAM-FILE",
        type=Path,
        help=(
            "the CCS file in BAM format can be optionally provided; "
            "otherwise it is computed. It is necessary to create the "
            "reference mapping between *hole numbers* and the DNA sequence "
            "of the corresponding fragment, or *molecule*. After being "
            "aligned, the file will be also used to determine the position "
            "of each molecule in the report of methylation states. If the "
            "CCS BAM file is provided, and any of the necessary aligned "
            "versions of it is not found, the CCS file will be aligned to "
            "be able to get the positions. If this option is not used, a "
            "CCS BAM will be generated from the original BAM file using "
            "the 'ccs' program"
        )
    )
)

_KEEP_TEMP_DIR = (
    ("--keep-temp-dir",),
    dict(
        action="store_true",
        help=("use this flag to make a copy of the temporary files generated")
    )
)

_MODIFICATION_TYPES = (
    ("-m", "--modification-types"),
    dict(
        default=DEFAULT_MODIFICATION_TYPE,
        nargs="+",
        metavar="MOD-TYPE",
        help=(
            "focus only in the requested modification types (default: "
            "%(default)s)"
        )
    )
)

_ONLY_PRODUCE_METHYLATION_REPORTS = (
    ("--only-produce-methylation-report",),
    dict(
        action="store_true",
        help=(
            "use this flag to only produce the methylation report from the "
            "per detection csv file (default: %(default)s)"
        )
    )
)

_USE_BLASR_ALIGNER = (
    ("--use-blasr-aligner",),
    dict(
        action="store_true",
        help=(
            "this option sets blasr as the aligner, instead of the default "
            f"aligner ({DEFAULT_ALIGNER_PROGRAM})"
        )
    )
)

_MAPPING_QUALITY_THRESHOLD = (
    ("--mapping-quality-threshold",),
    dict(
        default=None,
        type=int,
        metavar="NUM",
        choices=range(256),
        help=(
            "minimum mapping quality that each individual subread is required "
            "to have in order to pass the filters. The possible mapping "
            "quality values are positive integers in the range [0, 255] "
            "(default: half the estimated maximum value found in the aligned "
            "BAM file)."
        )
    )
)

# Options for bam-filter:

_INPUT_BAM_FILE_4FILTER = (
    ("input_bam_file",),
    dict(
        metavar=BAM_FILE_METAVAR,
        type=Path,
        help=INPUT_BAM_FILE_4FILTER_HELP
    )
)

_MIN_DNA_SEQ_LENGTH = (
    ("-l", "--min-dna-seq-length"),
    dict(
        default=DEFAULT_DNA_LEN_TH,
        type=int,
        metavar="NUM",
        help=(
            "minimum length of DNA sequence to be kept "
            "(default: %(default)s)"
        )
    )
)

_MIN_SUBREADS_PER_MOLECULE = (
    ("-r", "--min-subreads-per-molecule"),
    dict(
        default=DEFAULT_NUM_MOL_TH,
        type=int,
        metavar="NUM",
        help=(
            "minimum number of subreads per molecule to keep it (default: "
            "%(default)s)"
        )
    )
)

_QUALITY_THRESHOLD = (
    ("-q", "--quality-threshold"),
    dict(
        default=DEFAULT_QUAL_TH,
        type=int,
        metavar="NUM",
        choices=range(256),
        help=(
            "quality threshold of the sample. Between 0 (the lowest) and 255 "
            "(the highest) (default: %(default)s)"
        )
    )
)

_MAPPINGS = (
    ("-m", "--mappings"),
    dict(
        default="all",
        nargs="+",
        metavar="MAPPING",
        help=(
            "keep only the requested (space separated) list of mappings "
            "(default: keep %(default)s)"
        )
    )
)

_MIN_RELATIVE_MAPPING_RATIO = (
    ("-R", "--min-relative-mapping-ratio"),
    dict(
        default=DEFAULT_MINIMUM_MAPPING_RATIO,
        metavar="NUM",
        type=float,
        help=(
            "minimum ratio (wanted mappings/all mappings) to keep the "
            "subread (default: take all)"
        )
    )
)

# Common options:
_VERBOSE = (("-v", "--verbose"), dict(action="count", default=0))

_VERSION = (("--version",), dict(action="version", version=__version__))


# Full lists of options for each program:

SM_ANALYSIS_OPTS = [
    _INPUT_BAM_FILE,
    _FASTA,
    _IPD_MODEL,
    _ALIGNER_PROGRAM,
    _PBINDEX_PROGRAM,
    _IPDSUMMARY_PROGRAM,
    _CCS_PROGRAM,
    _NUM_SIMULTANEOUS_IPDSUMMARYS,
    _NUM_WORKERS_PER_IPDSUMMARY,
    _NPROCS_BLASR,
    _PARTITION,
    _CCS_BAM_FILE,
    _KEEP_TEMP_DIR,
    _MODIFICATION_TYPES,
    _ONLY_PRODUCE_METHYLATION_REPORTS,
    _USE_BLASR_ALIGNER,
    _MAPPING_QUALITY_THRESHOLD,
    _VERBOSE,
    _VERSION,
]

BAM_FILTER_OPTS = [
    _INPUT_BAM_FILE_4FILTER,
    _MIN_DNA_SEQ_LENGTH,
    _MIN_SUBREADS_PER_MOLECULE,
    _QUALITY_THRESHOLD,
    _MAPPINGS,
    _MIN_RELATIVE_MAPPING_RATIO,
    _VERBOSE,
    _VERSION
]
