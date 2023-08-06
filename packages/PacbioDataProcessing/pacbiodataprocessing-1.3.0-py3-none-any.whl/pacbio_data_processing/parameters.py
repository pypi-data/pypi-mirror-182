#######################################################################
#
# Copyright (C) 2021, 2022 David Palao
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

"""This module defines mediator classes to interact with user
given parameters.
"""

from pathlib import Path
import logging
import importlib.resources
from typing import Optional
from functools import cached_property

from .filters import filter_mappings_binary, filter_mappings_ratio
from . import __version__ as VERSION
from .utils import make_partition_prefix
from .constants import DEFAULT_ALIGNER_PROGRAM, DEFAULT_BLASR_PROGRAM


PARTITION_ERR_MSG_TEMPLATE = (
    "{err_msg} ('{raw_partition}'). Using default partition."
)


class ParametersBase:
    def __init__(self, cl_input):
        self._cl_input = cl_input

    def __getattr__(self, attr):
        return getattr(self._cl_input, attr)


class BamFilteringParameters(ParametersBase):
    """Mediator class: intermediary between the user input and the
    ``BamFilter`` instance.
    """

    def __str__(self):
        s = (
            f"Filtering '{self.input_bam_file}' to produce "
            f"'{self.out_bam_file}' with:\n"
            f"  minimun DNA sequence length: {self.min_dna_seq_length}\n"
            f"  minimun subreads per molecule: "
            f"{self.min_subreads_per_molecule}\n"
            f"  quality of sequencing: {self.quality_threshold}\n"
            f"  mappings: {self.mappings}\n"
            f"  min mapping ratio: {self.min_relative_mapping_ratio}\n"
        )
        return s

    @property
    def out_bam_file(self):
        base = self.input_bam_file.name
        new_base = "parsed." + base
        return self.input_bam_file.parent/new_base

    @property
    def limit_mappings(self):
        if self._cl_input.mappings != "all":
            return self._cl_input.mappings

    @property
    def filter_mappings(self):
        if self.min_relative_mapping_ratio:
            return filter_mappings_ratio
        return filter_mappings_binary

    @property
    def min_relative_mapping_ratio(self):
        ratio = self._cl_input.min_relative_mapping_ratio
        if ratio > 1:
            ratio = 1.0
        elif ratio < 0:
            ratio = 0.0
        return ratio


class SingleMoleculeAnalysisParameters(ParametersBase):
    """Mediator class: intermediary between the user input and the
    ``SingleMoleculeAnalysis`` instance.
    """

    def _make_out_filename(self, *, suff: str, pref: str = "") -> Path:
        base = self.input_bam_file.name
        new_base = "sm-analysis." + base
        if self.partition:
            partition, partitions = self.partition
            new_base = (
                make_partition_prefix(partition, partitions) + "." + new_base
            )
        new_name = self.input_bam_file.parent/(pref+new_base)
        if new_name.suffix != ".bam":
            suff = new_name.suffix+suff
        return new_name.with_suffix(suff)

    @property
    def joint_gff_filename(self):
        return self._make_out_filename(suff=".gff")

    @property
    def raw_detections_filename(self):
        return self._make_out_filename(suff=".csv")

    @property
    def summary_report_html_filename(self):
        return self._make_out_filename(suff=".html", pref="summary.")

    @property
    def partition_done_filename(self):
        return self._make_out_filename(suff=".done", pref=".")

    def _resolve_model_from_resources(self, model_name):
        container = importlib.resources.files("kineticsTools")
        return container/"resources"/f"{model_name}.npz.gz"

    @property
    def ipd_model(self) -> Optional[Path]:
        raw_model = self._cl_input.ipd_model
        if raw_model:
            model = Path(raw_model)
            if not model.is_file():
                model = self._resolve_model_from_resources(raw_model)
                if not model.is_file():
                    model = None
            return model

    @cached_property
    def partition(self) -> Optional[tuple[int, int]]:
        """It validates the input partition and interfaces with API
        clients.
        """
        raw_partition = self._cl_input.partition
        try:
            partition, partitions = [int(_) for _ in raw_partition.split(":")]
        except AttributeError:
            pass
        except ValueError:
            logging.error(
                PARTITION_ERR_MSG_TEMPLATE.format(
                    err_msg="Invalid syntax for the partition",
                    raw_partition=raw_partition
                )
            )
        else:
            positive = (partition > 0) and (partitions > 0)
            allowed_partition = partition <= partitions
            if positive and allowed_partition:
                return partition, partitions
            else:
                logging.error(
                    PARTITION_ERR_MSG_TEMPLATE.format(
                        err_msg="The given partition is not valid",
                        raw_partition=raw_partition
                    )
                )

    @property
    def aligner_path(self) -> Path:
        """The path to the aligner to be used. It depends on the choice
        made directly by the user through the ``-a`` option, and on the
        usage of the ``--use-blasr-aligner`` flag.
        """
        aligner = self._cl_input.aligner_path
        if self.use_blasr_aligner:
            if str(aligner) == DEFAULT_ALIGNER_PROGRAM:
                aligner = Path(DEFAULT_BLASR_PROGRAM)
        return aligner

    def __str__(self):
        s = (
            f"Starting 'sm-analysis' (version {VERSION}) with:\n"
            f"  Input BAM file:  '{self.input_bam_file}'\n"
            f"  Reference file:  '{self.fasta}'\n"
            f"  ipd program:  '{self.ipdsummary_path}'\n"
            f"  # ipd program instances:  {self.num_simultaneous_ipdsummarys}"
            f"\n"
            f"  # workers per ipd instance:  {self.num_workers_per_ipdsummary}"
            f"\n"
            f"  modification types:  {self.modification_types}\n"
            f"  aligner:  '{self.aligner_path}'\n"
        )
        if self.use_blasr_aligner:
            s += f"  # workers blasr:  {self.nprocs_blasr}\n"
        s += (
            f"  indexer:  '{self.pbindex_path}'\n"
            f"  ccs program:  '{self.ccs_path}'\n"
        )
        if self.ipd_model:
            s = s + f"  ipd model:  {self.ipd_model}\n"
        elif self._cl_input.ipd_model:
            # In this case the user entered the model but it wasn't found:
            logging.error(
                f"Model '{self._cl_input.ipd_model}' "
                "not found. Using default model"
            )
        if self.partition:
            s += f"  partition:  {self.partition[0]} of {self.partition[1]}\n"
        if self.CCS_bam_file:
            s += f"  CCS bam file:  '{self.CCS_bam_file}'\n"
        if self.keep_temp_dir:
            s += "  keep temp dir:  yes\n"
        if self.only_produce_methylation_report:
            s += "  only produce methylation report:  yes\n"
        if self.mapping_quality_threshold:
            s += ("  Mapping quality threshold:  "
                  f"{self.mapping_quality_threshold}\n"
            )
        return s
