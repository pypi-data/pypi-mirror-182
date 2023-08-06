#######################################################################
#
# Copyright (C) 2022 David Palao
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

import unittest
from unittest.mock import patch, mock_open, MagicMock, call
from datetime import datetime
import sys
import socket
from pathlib import Path
from dataclasses import dataclass
from collections import namedtuple, defaultdict
import random

from pandas import Series
from pandas.testing import assert_series_equal

from pacbio_data_processing.summary import (
    SummaryReport, DEFAULT_STYLE, BarsPlotAttribute, HistoryPlotAttribute,
    PositionCoverageHistory, MoleculeLenHistogram, PercAttribute,
    InputReferenceAttribute, MoleculeTypeBarsPlot, MappingQualityHistogram,
    AlignedBamAttribute, MappingQualityThresholdAttribute,
)
from pacbio_data_processing.templates import SUMMARY_REPORT_HTML_TEMPLATE
from pacbio_data_processing import __version__ as VERSION
from pacbio_data_processing.constants import (
    SM_ANALYSIS_EXE, STRAIGHT_VARIANT, PI_SHIFTED_VARIANT,
)
from pacbio_data_processing.utils import DNASeq
from pacbio_data_processing.methylation import METHYLATION_REPORT_HEADER


@dataclass
class FakeMolecule:
    molecule_id: bytes

    def __getitem__(self, item):
        return ""


FakeSubread = namedtuple(
    "FakeSubread",
    ("desc", "where", "name", "pos", "qual", "cigar", "a", "b", "c",
        "seq", "molecule_id")
)


REFERENCE = (
    "AAACCCTGCACGGCACGTAGTCTCGGAACTAATTCTAGCATTGACTCGTACCCACGAGTCGCCCCC"
    "ATCGACTTCTGCTTgatcTCGCCCTTCGCCCTCGATCTCGAACTCGTGGCCCTCCATGTGCAC"
    "TTTTTAATTGATCTCGCCCTTCGCCCTCGATCTCGAACTCGTGGATCTGTGCACGGATC"
)

METH_REPORT_TEST_ROWS = [
    METHYLATION_REPORT_HEADER,
    ['100', 'ACGGCACGTAGTCTCGGAACTAATTCTAGCATTGACTCGTACCCACGAGTCGCCCCC',
     '10', '66', '57', '28', '28', '64.8', '93.0', '1', '0', '', '',
     '', '', '', '', '', '', '', ''],
    ['600', 'CTGCTTGATCTCGCCCTTCGCCCTCGATCTCGAACTCGTGGCCCTCCATGTGCAC',
     '75', '129', '55', '30', '30', '64.3', '93.0', '1', '2', '81,100',
     '2', 'f,f', '49.4', '60.0', '3.61', '7.41', '6.0', '43.0', '28'],
    ['610', 'GCTTGATCTCGCCCTTCGCCCTCGATCTCGAACTCGTGGCCCTCCATGTGCAC',
     '77', '129', '53', '20', '21', '34.3', '83.0', '1', '2', '81,100',
     '2', 'f,+', '49.3', '61.1', '4.31', '6.77', '5.4', '41.0', '26'],
    ['700', 'AATTGATCTCGCCCTTCGCCCTCGATCTCGAACTCGTGGATCTGTGCAC',
     '135', '183', '49', '22', '22', '43.3', '92.0', '1', '3', '139,158,173',
     '2', '0,+,-', '35.3', '51.5', '5.35', '5.75', '6.6', '46.3', '37'],
]

ALIGNED_CCS_BAM_LINES = (
    FakeSubread(
        b"", b"", b"", b"1", b"",
        b"129=", b"", b"", b"",
        (b"AAACCCTGCACGGCACGTAGTCTCGGAACTAATTCTAGCATTGACTCGTACCCACGAGTCGCCCCC"
         b"ATCGACTTCTGCTTGATCTCGCCCTTCGCCCTCGATCTCGAACTCGTGGCCCTCCATGTGCAC"),
        b"514"),
    FakeSubread(
        b"", b"", b"", b"1", b"",
        b"128=1X", b"", b"", b"",
        (b"AAACCCTGCACGGCACGTAGTCTCGGAACTAATTCTAGCATTGACTCGTACCCACGAGTCGCCCCC"
         b"ATCGACTTCTGCTTGATCTCGCCCTTCGCCCTCGATCTCGAACTCGTGGCCCTCCATGTGCAA"),
        b"514"),
    FakeSubread(
        b"", b"", b"", b"130", b"",
        b"2=3X53=", b"", b"", b"",
        b"TTGGGAATTGATCTCGCCCTTCGCCCTCGATCTCGAACTCGTGGATCTGTGCACGGAT",
        b"1514"),
)

PI_SHIFTED_ALIGNED_CCS_BAM_LINES = (
    FakeSubread(
        b"", b"", b"", b"95", b"",
        b"128=1X", b"", b"", b"",
        (b"AAACCCTGCACGGCACGTAGTCTCGGAACTAATTCTAGCATTGACTCGTACCCACGAGTCGCCCCC"
         b"ATCGACTTCTGCTTGATCTCGCCCTTCGCCCTCGATCTCGAACTCGTGGCCCTCCATGTGCAA"),
        b"514"),
    FakeSubread(
        b"", b"", b"", b"36", b"",
        b"58=", b"", b"", b"",
        b"TTTTTAATTGATCTCGCCCTTCGCCCTCGATCTCGAACTCGTGGATCTGTGCACGGAT",
        b"1514"),
    FakeSubread(
        b"", b"", b"", b"144", b"",
        b"30=2X20=", b"", b"", b"",
        b"ACCCACGAGTCGCCCCCATCGACTTCTGCTCCATCTCGCCCTTCGCCCTCGA",
        b"11111"),
)

PI_SHIFTED_ALIGNED_CCS_BAM_LINES_ISSUE_62 = (
    FakeSubread(
        b"", b"", b"", b"90", b"",
        b"95=", b"", b"", b"",
        (b"GGATCAAACCCTGCACGGCACGTAGTCTCGGAACTAATTCTAGCATTGACTCGTACCCACGAGTC"
         b"GCCCCCATCGACTTCTGCTTgatcTCGCCC"),
        b"23455"),  # This FakeSubread ensures that issue #62 is fixed
)

ALIGNED_BAM_LINES = tuple(
    [FakeSubread(b"", b"", b"", b"46", b"",
                 b"30=2X20=", b"", b"", b"",
                 b"ACCCACGAGTCGCCCCCATCGACTTCTGCTCCATCTCGCCCTTCGCCCTCGA",
                 b"11111") for i in range(24)]
) + tuple(
    [FakeSubread(b"", b"", b"", b"47", b"",
                 b"30=2X20=", b"", b"", b"",
                 b"ACCCACGAGTCGCCCCCATCGACTTCTGCTCCATCTCGCCCTTCGCCCTCGA",
                 b"11111") for i in range(100)]
)


@patch("pacbio_data_processing.summary.pandas")
@patch("pacbio_data_processing.summary.make_histogram")
@patch("pacbio_data_processing.summary.make_barsplot")
@patch("pacbio_data_processing.summary.make_multi_histogram")
@patch("pacbio_data_processing.summary.make_rolling_history")
@patch("pacbio_data_processing.summary.BamFile")
class SummaryReportTestCase(unittest.TestCase):
    def setUp(self):
        self.reference = DNASeq(
            REFERENCE, name="U096.3",
            description="U096.3 complete genome",
        )
        self.mapq_series = Series([46]*24+[47]*100)
        self.expected_data = {
            "style": DEFAULT_STYLE,
            "version": VERSION,
            "when": datetime.now().isoformat(timespec="minutes"),
            "program": SM_ANALYSIS_EXE,
            "clos": " ".join(sys.argv[1:]),
            "hostname": socket.gethostname(),
            "methylation_report": "a/b.c",
            "raw_detections": "q",
            "gff_result": "h.gff",
            "input_bam": "my.bam",
            "input_bam_size": 526039,
            "full_md5sum": "1634e047cda4cd3d547dde4e0a974181",
            "body_md5sum": "93a7f9bcb673053ab874e80d47fae941",
            "input_reference": "myc.fasta",
            "reference_name": "U096.3 complete genome",
            "reference_base_pairs": 188,
            "reference_md5sum": "24d9a40bc45db50ef74fabdd34e04b8b",
            "mols_ini": 123,
            "subreads_ini": 1235,
            "subreads_aligned_ini": 124,
            "mols_dna_mismatches": 3,
            "perc_mols_dna_mismatches": "2.44",
            "subreads_dna_mismatches": 229,
            "perc_subreads_dna_mismatches": "18.54",
            "filtered_out_mols": 2,
            "perc_filtered_out_mols": "1.63",
            "filtered_out_subreads": 62,
            "perc_filtered_out_subreads": "5.02",
            "faulty_mols": 0,
            "perc_faulty_mols": "0.00",
            "faulty_subreads": 0,
            "perc_faulty_subreads": "0.00",
            "mols_in_meth_report": 4,
            "perc_mols_in_meth_report": "3.25",
            "subreads_in_meth_report": 201,
            "perc_subreads_in_meth_report": "16.28",
            "mols_in_meth_report_with_gatcs": 3,
            "perc_mols_in_meth_report_with_gatcs": "2.44",
            "subreads_in_meth_report_with_gatcs": 145,
            "perc_subreads_in_meth_report_with_gatcs": "11.74",
            "mols_in_meth_report_without_gatcs": 1,
            "perc_mols_in_meth_report_without_gatcs": "0.81",
            "subreads_in_meth_report_without_gatcs": 56,
            "perc_subreads_in_meth_report_without_gatcs": "4.53",
            "molecule_type_bars": "figures/molecule_type_bars.png",
            "molecule_len_histogram": "figures/molecule_length_histogram.png",
            "mapping_quality_histogram": (
                "figures/mapping_quality_histogram.png"),
            "mols_used_in_aligned_ccs": 118,
            "perc_mols_used_in_aligned_ccs": "95.93",
            "subreads_used_in_aligned_ccs": 944,
            "perc_subreads_used_in_aligned_ccs": "76.44",
            "all_positions_in_bam": 187,
            "perc_all_positions_in_bam": "99.47",
            "all_positions_not_in_bam": 1,
            "perc_all_positions_not_in_bam": "0.53",
            "all_positions_in_meth": 161,
            "perc_all_positions_in_meth": "85.64",
            "all_positions_not_in_meth": 27,
            "perc_all_positions_not_in_meth": "14.36",
            "position_coverage_bars": "figures/position_coverage_bars.png",
            "position_coverage_history": (
                "figures/position_coverage_history.png"),
            "total_gatcs_in_ref": 6,
            "all_gatcs_identified_in_bam": 5,
            "perc_all_gatcs_identified_in_bam": "83.33",
            "all_gatcs_not_identified_in_bam": 1,
            "perc_all_gatcs_not_identified_in_bam": "16.67",
            "all_gatcs_in_meth": 5,
            "perc_all_gatcs_in_meth": "83.33",
            "all_gatcs_not_in_meth": 1,
            "perc_all_gatcs_not_in_meth": "16.67",
            "gatc_coverage_bars": "figures/gatc_coverage_bars.png",
            "max_possible_methylations": 7,
            "fully_methylated_gatcs": 3,
            "fully_methylated_gatcs_wrt_meth": "42.86",
            "fully_unmethylated_gatcs": 1,
            "fully_unmethylated_gatcs_wrt_meth": "14.29",
            "hemi_methylated_gatcs": 3,
            "hemi_methylated_gatcs_wrt_meth": "42.86",
            "hemi_plus_methylated_gatcs": 2,
            "hemi_plus_methylated_gatcs_wrt_meth": "28.57",
            "hemi_minus_methylated_gatcs": 1,
            "hemi_minus_methylated_gatcs_wrt_meth": "14.29",
            "meth_type_bars": "figures/meth_type_bars.png",
            "mapping_qualities": self.mapq_series,
            "mapping_quality_threshold": 47,
            "subreads_with_low_mapq": 24,
            "perc_subreads_with_low_mapq": "19.35",
            "subreads_with_high_mapq": 100,
            "perc_subreads_with_high_mapq": "80.65",
        }
        self.all_aligned_ccs_bam_files = {
            STRAIGHT_VARIANT: "blsr_ccs.bam",
            PI_SHIFTED_VARIANT: "pi-shifted_blsr_ccs.bam"
        }
        self.only_straight_expected_data = self.expected_data.copy()
        self.only_straight_expected_data.update(
            {
                "all_positions_in_bam": 129,
                "perc_all_positions_in_bam": "68.62",
                "all_positions_not_in_bam": 59,
                "perc_all_positions_not_in_bam": "31.38",
                "all_gatcs_identified_in_bam": 2,
                "perc_all_gatcs_identified_in_bam": "33.33",
                "all_gatcs_not_identified_in_bam": 4,
                "perc_all_gatcs_not_identified_in_bam": "66.67",
            }
        )
        self.only_straight_aligned_ccs_bam_files = {
            STRAIGHT_VARIANT: "blsr_ccs.bam",
            PI_SHIFTED_VARIANT: None
        }
        self.expected_data_issue_62 = self.expected_data.copy()
        self.expected_data_issue_62.update(
            {
                "all_gatcs_identified_in_bam": 6,
                "perc_all_gatcs_identified_in_bam": "100.00",
                "all_gatcs_not_identified_in_bam": 0,
                "perc_all_gatcs_not_identified_in_bam": "0.00",
                "all_positions_in_bam": 188,
                "perc_all_positions_in_bam": "100.00",
                "all_positions_not_in_bam": 0,
                "perc_all_positions_not_in_bam": "0.00",
            }
        )
        self.expected_data_issue_87 = self.expected_data.copy()
        self.expected_data_issue_87.update(
            {
                "all_gatcs_identified_in_bam": 6,
                "perc_all_gatcs_identified_in_bam": "100.00",
                "all_gatcs_not_identified_in_bam": 0,
                "perc_all_gatcs_not_identified_in_bam": "0.00",
                "all_positions_in_bam": 188,
                "perc_all_positions_in_bam": "100.00",
                "all_positions_not_in_bam": 0,
                "perc_all_positions_not_in_bam": "0.00",
                "mols_dna_mismatches": 2,
                "perc_mols_dna_mismatches": "1.63",
                "subreads_dna_mismatches": 166,
                "perc_subreads_dna_mismatches": "13.44",
                "filtered_out_mols": 1,
                "perc_filtered_out_mols": "0.81",
                "filtered_out_subreads": 32,
                "perc_filtered_out_subreads": "2.59",
                "faulty_mols": 2,
                "perc_faulty_mols": "1.63",
                "faulty_subreads": 93,
                "perc_faulty_subreads": "7.53",
            }
        )
        self.expected_data_no_problems = self.expected_data.copy()
        self.expected_data_no_problems.update(
            {
                "all_gatcs_identified_in_bam": 6,
                "perc_all_gatcs_identified_in_bam": "100.00",
                "all_gatcs_not_identified_in_bam": 0,
                "perc_all_gatcs_not_identified_in_bam": "0.00",
                "all_positions_in_bam": 188,
                "perc_all_positions_in_bam": "100.00",
                "all_positions_not_in_bam": 0,
                "perc_all_positions_not_in_bam": "0.00",
                "mols_dna_mismatches": 0,
                "perc_mols_dna_mismatches": "0.00",
                "subreads_dna_mismatches": 0,
                "perc_subreads_dna_mismatches": "0.00",
                "filtered_out_mols": 0,
                "perc_filtered_out_mols": "0.00",
                "filtered_out_subreads": 0,
                "perc_filtered_out_subreads": "0.00",
                "faulty_mols": 0,
                "perc_faulty_mols": "0.00",
                "faulty_subreads": 0,
                "perc_faulty_subreads": "0.00",
            }
        )

    def create_summary_report(
            self, pBamFile, pi_shifted_lines_extra=(),
            fig_prefix=None,
    ):
        fake_bam = MagicMock()
        ccs_bam = MagicMock()
        fake_pbmm2_bam = MagicMock()
        ccs_bam.__iter__.side_effect = lambda: iter(ALIGNED_CCS_BAM_LINES)
        pi_shifted_ccs_bam = MagicMock()
        pi_shifted_ccs_bam.__iter__.side_effect = (
            lambda: iter(
                PI_SHIFTED_ALIGNED_CCS_BAM_LINES+pi_shifted_lines_extra
            )
        )

        def make_bam(name):
            if name == "my.bam":
                bam = fake_bam
            elif name == "blsr_ccs.bam":
                bam = ccs_bam
            elif name == "pi-shifted_blsr_ccs.bam":
                bam = pi_shifted_ccs_bam
            elif name == "pbmm2.my.bam":
                bam = fake_pbmm2_bam
            elif name is None:
                bam = None
            else:
                bam = MagicMock()
            return bam
        pBamFile.side_effect = make_bam
        fake_bam.size_in_bytes = 526039
        fake_bam.full_md5sum = "1634e047cda4cd3d547dde4e0a974181"
        fake_bam.md5sum_body = "93a7f9bcb673053ab874e80d47fae941"
        fake_bam.num_molecules = 123
        fake_bam.num_subreads = 1235
        fake_molecules = (
            [FakeMolecule(molecule_id=b"2")]*104 +
            [FakeMolecule(molecule_id=b"22")]*63 +
            [FakeMolecule(molecule_id=b"202")]*62 +
            [FakeMolecule(molecule_id=b"324")]*32 +
            [FakeMolecule(molecule_id=b"567")]*30 +
            [FakeMolecule(
                molecule_id=str(i).encode()
                ) for i in range(1000, 1118) for j in range(8)]
        )
        fake_bam.__iter__.side_effect = lambda: iter(fake_molecules)
        self.reference.fasta_name = "myc.fasta"
        series = MagicMock()
        series.return_value = self.mapq_series
        with patch("pacbio_data_processing.summary.pandas.Series", new=series):
            if fig_prefix:
                report = SummaryReport(
                    "my.bam", "pbmm2.my.bam", self.reference,
                    figures_prefix=fig_prefix)
            else:
                report = SummaryReport(
                    "my.bam", "pbmm2.my.bam", self.reference)
        report.mapping_quality_threshold = 47
        return report

    def test_figures_dir_created(
            self, pBamFile, prolling, pmultihist, pbars, phist, pd):
        with patch("pacbio_data_processing.summary.Path") as pPath:
            SummaryReport("my.bam", "pbmm2.my.bam", self.reference)
        pPath.assert_called_once_with("figures")
        pPath.return_value.mkdir.assert_called_once_with(exist_ok=True)

    def test_save_writes_rendered_template(
            self, pBamFile, prolling, pmultihist, pbars, phist, pd):
        pd.Series.return_value = Series((8, 23, 58, 12, 60))
        s = self.create_summary_report(pBamFile)
        s._data["mols_ini"] = 123
        s._data["subreads_ini"] = 1235
        s._data["subreads_aligned_ini"] = 1124
        mopen = mock_open()
        with patch("pacbio_data_processing.summary.open", mopen):
            with patch("pacbio_data_processing.summary.csv.reader") as preader:
                preader.return_value = iter(METH_REPORT_TEST_ROWS)
                s.methylation_report = Path("w")
        s.raw_detections = Path("q")
        s.gff_result = Path("h.gff")
        placeholders_needed = (
            "perc_mols_dna_mismatches",
            "perc_subreads_dna_mismatches",
            "perc_filtered_out_mols",
            "perc_filtered_out_subreads",
            "perc_all_gatcs_identified_in_bam",
            "perc_all_gatcs_not_identified_in_bam",
            "perc_mols_used_in_aligned_ccs",
            "perc_subreads_used_in_aligned_ccs",
            "perc_all_positions_in_bam",
            "perc_all_positions_not_in_bam",
        )
        attrs_needed = {
            "mols_used_in_aligned_ccs": 23,
            "subreads_used_in_aligned_ccs": 241,
            "mols_dna_mismatches": 4,
            "subreads_dna_mismatches": 45,
            "filtered_out_mols": 3,
            "filtered_out_subreads": 31,
            "faulty_mols": 0,
            "faulty_subreads": 0,
            "all_positions_in_bam": 456,
            "all_positions_not_in_bam": 24,
            "all_gatcs_identified_in_bam": 31,
            "all_gatcs_not_identified_in_bam": 22,
        }
        for attr in attrs_needed:
            s._data[attr] = None
        for attr, value in attrs_needed.items():
            s._data[attr] = value
        mopen = mock_open()
        s.aligned_ccs_bam_files = {
            STRAIGHT_VARIANT: "blsr_ccs.bam",
            PI_SHIFTED_VARIANT: "pi-shifted_blsr_ccs.bam"
        }
        with (
                patch("pacbio_data_processing.summary.open", mopen),
                patch(
                    "pacbio_data_processing.summary.SummaryReport"
                    ".ready_to_go") as pready_to_go):
            pready_to_go.return_value = True
            s.save("my_file_name.html")
        mopen.assert_called_once_with("my_file_name.html", "w")
        handle = mopen()
        handle.write.assert_called_once_with(s.as_html)

    def test_as_html(
            self, pBamFile, prolling, pmultihist, pbars, phist, pd):
        self.maxDiff = None
        s = self.create_summary_report(pBamFile)
        pBamFile.assert_has_calls(
            [call("my.bam"), call("pbmm2.my.bam")],
            any_order=True
        )
        mopen = mock_open()
        with patch("pacbio_data_processing.summary.open", mopen):
            with patch("pacbio_data_processing.summary.csv.reader") as preader:
                preader.return_value = iter(METH_REPORT_TEST_ROWS)
                s.methylation_report = Path("a/b.c")
        s.raw_detections = Path("q")
        s.gff_result = Path("h.gff")
        s.mols_dna_mismatches = {2, 22, 202}
        s.filtered_out_mols = {324, 567}
        s.mols_used_in_aligned_ccs = set(range(1000, 1118))
        s.aligned_ccs_bam_files = self.all_aligned_ccs_bam_files
        self.assertEqual(
            s.as_html,
            SUMMARY_REPORT_HTML_TEMPLATE.format(**self.expected_data)
        )
        s.aligned_ccs_bam_files = self.only_straight_aligned_ccs_bam_files
        self.assertEqual(
            s.as_html,
            SUMMARY_REPORT_HTML_TEMPLATE.format(
                **self.only_straight_expected_data)
        )

    def test_as_html_issue_62(
            self, pBamFile, prolling, pmultihist, pbars, phist, pd):
        self.maxDiff = None
        s = self.create_summary_report(
            pBamFile,
            pi_shifted_lines_extra=PI_SHIFTED_ALIGNED_CCS_BAM_LINES_ISSUE_62
        )
        pBamFile.assert_has_calls(
            [call("my.bam"), call("pbmm2.my.bam")],
            any_order=True
        )
        mopen = mock_open()
        with patch("pacbio_data_processing.summary.open", mopen):
            with patch("pacbio_data_processing.summary.csv.reader") as preader:
                preader.return_value = iter(METH_REPORT_TEST_ROWS)
                s.methylation_report = Path("a/b.c")
        s.raw_detections = Path("q")
        s.gff_result = Path("h.gff")
        s.mols_dna_mismatches = {2, 22, 202}
        s.filtered_out_mols = {324, 567}
        s.mols_used_in_aligned_ccs = set(range(1000, 1118))
        s.aligned_ccs_bam_files = self.all_aligned_ccs_bam_files
        self.assertEqual(
            s.as_html,
            SUMMARY_REPORT_HTML_TEMPLATE.format(**self.expected_data_issue_62)
        )

    def test_read_only_attributes(
            self, pBamFile, prolling, pmultihist, pbars, phist, pd):
        fake_bam = pBamFile.return_value
        fake_bam.size_in_bytes = 526
        fake_bam.num_subreads = 1235
        fake_bam.full_md5sum = "1634e047cda4cd3d547dde4e0a974181"
        fake_bam.md5sum_body = "93a7f9bcb673053ab874e80d47fae941"
        fake_bam.num_molecules = 123
        fake_bam.num_subreads = 1235
        series = MagicMock()
        series.return_value = self.mapq_series
        with patch("pacbio_data_processing.summary.pandas.Series", new=series):
            s = SummaryReport("my.bam", "pbmm2.my.bam", self.reference)
        self.assertEqual(s.input_bam_size, 526)
        self.assertEqual(s.full_md5sum, "1634e047cda4cd3d547dde4e0a974181")
        self.assertEqual(s.body_md5sum, "93a7f9bcb673053ab874e80d47fae941")
        self.assertEqual(s.reference_name, "U096.3 complete genome")
        self.assertEqual(s.reference_base_pairs, 188)
        self.assertEqual(
            s.reference_md5sum, "24d9a40bc45db50ef74fabdd34e04b8b")
        self.assertEqual(s.mols_ini, 123)
        self.assertEqual(s.subreads_ini, 1235)
        self.assertEqual(s.subreads_aligned_ini, 124)
        assert_series_equal(s.mapping_qualities, self.mapq_series)
        trials = {
            "input_bam_size": 4,
            "full_md5sum": "ddd",
            "body_md5sum": "222",
            "reference_name": "hu",
            "reference_base_pairs": 5,
            "reference_md5sum": "636362",
            "mols_ini": 2,
            "subreads_ini": 39,
            "subreads_aligned_ini": 22,
            "perc_mols_dna_mismatches": "3.42",
            "subreads_dna_mismatches": 2209,
            "perc_subreads_dna_mismatches": "6.22",
            "perc_filtered_out_mols": "23.63",
            "filtered_out_subreads": 246,
            "perc_filtered_out_subreads": "23.72",
            "perc_faulty_mols": "12.23",
            "faulty_subreads": 456,
            "perc_faulty_subreads": "43.02",
            "mols_in_meth_report": 3,
            "perc_mols_in_meth_report": "23.25",
            "subreads_in_meth_report": 21,
            "perc_subreads_in_meth_report": "6.28",
            "mols_in_meth_report_with_gatcs": 5,
            "perc_mols_in_meth_report_with_gatcs": "7.84",
            "subreads_in_meth_report_with_gatcs": 15,
            "perc_subreads_in_meth_report_with_gatcs": "81.74",
            "mols_in_meth_report_without_gatcs": 61,
            "perc_mols_in_meth_report_without_gatcs": "60.81",
            "subreads_in_meth_report_without_gatcs": 59,
            "perc_subreads_in_meth_report_without_gatcs": "74.53",
            "perc_mols_used_in_aligned_ccs": "5.21",
            "subreads_used_in_aligned_ccs": 68,
            "perc_subreads_used_in_aligned_ccs": "5.22",
            "all_positions_in_bam": 17,
            "perc_all_positions_in_bam": "29.47",
            "all_positions_not_in_bam": 12,
            "perc_all_positions_not_in_bam": "2.53",
            "all_positions_in_meth": 162,
            "perc_all_positions_in_meth": "85.34",
            "all_positions_not_in_meth": 25,
            "perc_all_positions_not_in_meth": "16.36",
            "molecule_type_bars": "figures/molecule_type_bars2.png",
            "molecule_len_histogram": "figures/molecule_l_histogram.png",
            "mapping_quality_histogram": "figures/mapq_histogram.png",
            "position_coverage_bars": "figures/position_coverage_bars.jpeg",
            "position_coverage_history": "figures/beautiful_flower.png",
            "total_gatcs_in_ref": 8,
            "all_gatcs_identified_in_bam": 4,
            "perc_all_gatcs_identified_in_bam": "83.34",
            "all_gatcs_not_identified_in_bam": 14,
            "perc_all_gatcs_not_identified_in_bam": "46.67",
            "all_gatcs_in_meth": 8,
            "perc_all_gatcs_in_meth": "83.43",
            "all_gatcs_not_in_meth": 15,
            "perc_all_gatcs_not_in_meth": "15.67",
            "gatc_coverage_bars": "figures/gatc_coverage_hist.png",
            "max_possible_methylations": 73,
            "fully_methylated_gatcs": 33,
            "fully_methylated_gatcs_wrt_meth": "43.86",
            "fully_unmethylated_gatcs": 13,
            "fully_unmethylated_gatcs_wrt_meth": "34.29",
            "hemi_methylated_gatcs": 6,
            "hemi_methylated_gatcs_wrt_meth": "62.86",
            "hemi_plus_methylated_gatcs": 26,
            "hemi_plus_methylated_gatcs_wrt_meth": "26.57",
            "hemi_minus_methylated_gatcs": 16,
            "hemi_minus_methylated_gatcs_wrt_meth": "14.49",
            "meth_type_bars": None,
            "mapping_qualities": (3, 4),
        }
        for attr, value in trials.items():
            with self.assertRaises(AttributeError) as cm:
                setattr(s, attr, value)
            self.assertEqual(
                str(cm.exception),
                f"attribute '{attr}' cannot be set directly"
            )

    def test_plots_generated(
            self, pBamFile, prolling, pmultihist, pbars, phist, pd):
        s = self.create_summary_report(pBamFile)
        pBamFile.assert_has_calls(
            [call("my.bam"), call("pbmm2.my.bam")],
            any_order=True
        )
        mopen = mock_open()
        with patch("pacbio_data_processing.summary.open", mopen):
            with patch("pacbio_data_processing.summary.csv.reader") as preader:
                preader.return_value = iter(METH_REPORT_TEST_ROWS)
                s.methylation_report = Path("a/b.c")
        s.raw_detections = Path("q")
        s.gff_result = Path("h.gff")
        s.mapping_quality_threshold = 35
        pd.Series.return_value = (8, 23, 58, 12, 60)
        s.mols_dna_mismatches = {2, 22, 202}
        s.filtered_out_mols = {324, 567}
        s.mols_used_in_aligned_ccs = set(range(1000, 1118))
        s.aligned_ccs_bam_files = {
            STRAIGHT_VARIANT: "blsr_ccs.bam",
            PI_SHIFTED_VARIANT: "pi-shifted_blsr_ccs.bam"
        }
        with patch("pacbio_data_processing.summary.open", mopen):
            s.save("whatever.html")
        pbars.assert_has_calls(
            [
                call(
                    pd.DataFrame.return_value,
                    "Processed molecules and subreads",
                    "figures/molecule_type_bars.png"
                ),
                call(
                    pd.DataFrame.return_value,
                    "Position coverage in BAM file and Methylation report",
                    "figures/position_coverage_bars.png"
                ),
                call(
                    pd.DataFrame.return_value,
                    "GATCs in BAM file and Methylation report",
                    "figures/gatc_coverage_bars.png"
                ),
                call(
                    pd.DataFrame.return_value,
                    "Methylation types in methylation report",
                    "figures/meth_type_bars.png"
                ),
            ]
        )
        pmultihist.assert_called_once_with(
            {
                "Initial subreads": pd.Series.return_value,
                "Analyzed molecules": (
                    pd.read_csv.return_value.__getitem__.return_value)
            },
            "Initial subreads and analyzed molecule length histogram",
            "figures/molecule_length_histogram.png", True,
        )
        phist.assert_called_once_with(
            pd.Series.return_value,
            "Mapping quality histogram of subreads in the aligned input BAM",
            "figures/mapping_quality_histogram.png", True,
            61, (False, True), 35, "mapping quality threshold"
        )
        prolling.assert_called_once_with(
            {i: 0 for i in range(
                1, self.expected_data["reference_base_pairs"]+1)},
            "Sequencing positions covered by analyzed molecules",
            "figures/position_coverage_history.png", False,
        )

    def test_save_calls__pre_save(
            self, pBamFile, prolling, pmultihist, pbars, phist, pd):
        s = self.create_summary_report(pBamFile)
        with patch("pacbio_data_processing.summary."
                   "SummaryReport._pre_save") as ppresave:
            with self.assertRaises(Exception):
                s.save("whatever.html")
            ppresave.assert_called_once_with()

    def test_switch_on_method(
            self, pBamFile, prolling, pmultihist, pbars, phist, pd):
        s = self.create_summary_report(pBamFile)
        self.assertFalse(s._primary_attributes["Iloveyou"])
        s.switch_on("Iloveyou")
        self.assertTrue(s._primary_attributes["Iloveyou"])

    def test_ready_to_go(
            self, pBamFile, prolling, pmultihist, pbars, phist, pd):
        s = self.create_summary_report(pBamFile)
        self.assertFalse(s.ready_to_go("data1", "data5"))
        s.switch_on("data1")
        self.assertFalse(s.ready_to_go("data1", "data5"))
        self.assertTrue(s.ready_to_go("data1"))
        s.switch_on("wah")
        self.assertFalse(s.ready_to_go("data1", "data5"))
        self.assertTrue(s.ready_to_go("data1"))
        self.assertTrue(s.ready_to_go("wah"))
        s.switch_on("data5")
        self.assertTrue(s.ready_to_go("data1", "data5"))
        self.assertTrue(s.ready_to_go("data1", "data5", "wah"))
        self.assertTrue(s.ready_to_go("data1"))
        self.assertTrue(s.ready_to_go("data5"))
        self.assertTrue(s.ready_to_go("data1"))

    def test_getitem(
            self, pBamFile, prolling, pmultihist, pbars, phist, pd):
        s = self.create_summary_report(pBamFile)
        with self.assertRaises(KeyError):
            s["incredible"]
        s.incredible = 8
        self.assertEqual(s["incredible"], 8)
        s._data["incredible"] = 2348
        self.assertEqual(s["incredible"], 2348)

    def test_keys(
            self, pBamFile, prolling, pmultihist, pbars, phist, pd):
        s = self.create_summary_report(pBamFile)
        pBamFile.return_value.side_effect = TypeError
        s.bam = pBamFile.return_value
        s.gff_result = "ssh"
        s.raw_detections = "xk"
        s._data["aligned_bam"] = pBamFile.return_value
        s._data["methylation_report"] = "moqui"
        numeric_keys = [
            "all_gatcs_in_meth", "filtered_out_mols",
            "mols_used_in_aligned_ccs", "subreads_in_meth_report_with_gatcs",
            "hemi_plus_methylated_gatcs", "all_positions_in_meth",
            "subreads_dna_mismatches", "mols_in_meth_report",
            "mols_dna_mismatches", "fully_unmethylated_gatcs",
            "hemi_methylated_gatcs", "mols_in_meth_report_with_gatcs",
            "subreads_in_meth_report", "filtered_out_subreads",
            "faulty_subreads",
            "hemi_minus_methylated_gatcs", "max_possible_methylations",
            "subreads_in_meth_report_without_gatcs",
            "subreads_used_in_aligned_ccs", "all_positions_not_in_meth",
            "all_gatcs_identified_in_bam", "all_gatcs_not_in_meth",
            "fully_methylated_gatcs", "all_gatcs_not_identified_in_bam",
            "mols_in_meth_report_without_gatcs", "all_positions_in_bam",
            "all_positions_not_in_bam", "aligned_ccs_bam_files",
            "subreads_aligned_ini"
        ]
        for key in numeric_keys:
            s._data[key] = random.randint(0, 1000)
        for key in s.keys():
            print(f"{key=}")
            with self.assertRaises(TypeError):
                s[key]()

    def test_len(self, pBamFile, prolling, pmultihist, pbars, phist, pd):
        s = self.create_summary_report(pBamFile)
        with patch("pacbio_data_processing.summary.SummaryReport.keys"
                   ) as pkeys:
            pkeys.return_value = set(range(489))
            self.assertEqual(len(s), 489)

    def test_iter(self, pBamFile, prolling, pmultihist, pbars, phist, pd):
        s = self.create_summary_report(pBamFile)
        s._data["α"] = "a"
        s._data["β"] = "B"
        with patch("pacbio_data_processing.summary.SummaryReport.keys"
                   ) as pkeys:
            pkeys.return_value = {"α", "β"}
            items = list(s)
            items.sort()
            self.assertEqual(items, ["B", "a"])

    def test_figure_files_with_prefix_issue_86(
            self, pBamFile, prolling, pmultihist, pbars, phist, pd):
        pref = "mypref."
        prefixed_figures = {
            "molecule_type_bars": f"figures/{pref}molecule_type_bars.png",
            "molecule_len_histogram": (
                f"figures/{pref}molecule_length_histogram.png"),
            "mapping_quality_histogram": (
                f"figures/{pref}mapping_quality_histogram.png"),
            "position_coverage_bars": (
                f"figures/{pref}position_coverage_bars.png"),
            "position_coverage_history": (
                f"figures/{pref}position_coverage_history.png"),
            "gatc_coverage_bars": (
                f"figures/{pref}gatc_coverage_bars.png"),
            "meth_type_bars": (
                f"figures/{pref}meth_type_bars.png"),
        }
        with patch("pacbio_data_processing.summary.Path"):
            r = SummaryReport(
                "my.bam", "pbmm2.my.bam", self.reference, figures_prefix=pref
            )
        for fig_attr, file_name in prefixed_figures.items():
            self.assertEqual(r[fig_attr], file_name)

    def test_report_contains_stats_on_faulty_mols_issue_87(
            self, pBamFile, prolling, pmultihist, pbars, phist, pd):
        self.maxDiff = None
        s = self.create_summary_report(
            pBamFile,
            pi_shifted_lines_extra=PI_SHIFTED_ALIGNED_CCS_BAM_LINES_ISSUE_62
        )
        pBamFile.assert_has_calls(
            [call("my.bam"), call("pbmm2.my.bam")],
            any_order=True
        )
        mopen = mock_open()
        with patch("pacbio_data_processing.summary.open", mopen):
            with patch("pacbio_data_processing.summary.csv.reader") as preader:
                preader.return_value = iter(METH_REPORT_TEST_ROWS)
                s.methylation_report = Path("a/b.c")
        s.raw_detections = Path("q")
        s.gff_result = Path("h.gff")
        s.mols_dna_mismatches = {2, 202}
        s.filtered_out_mols = {324}
        s.faulty_mols = {22, 567}
        s.mols_used_in_aligned_ccs = set(range(1000, 1118))
        s.aligned_ccs_bam_files = self.all_aligned_ccs_bam_files
        self.assertEqual(
            s.as_html,
            SUMMARY_REPORT_HTML_TEMPLATE.format(**self.expected_data_issue_87)
        )

    def test_report_without_faulty_missing_or_mismatches(
            self, pBamFile, prolling, pmultihist, pbars, phist, pd):
        self.maxDiff = None
        s = self.create_summary_report(
            pBamFile,
            pi_shifted_lines_extra=PI_SHIFTED_ALIGNED_CCS_BAM_LINES_ISSUE_62
        )
        pBamFile.assert_has_calls(
            [call("my.bam"), call("pbmm2.my.bam")],
            any_order=True
        )
        mopen = mock_open()
        with patch("pacbio_data_processing.summary.open", mopen):
            with patch("pacbio_data_processing.summary.csv.reader") as preader:
                preader.return_value = iter(METH_REPORT_TEST_ROWS)
                s.methylation_report = Path("a/b.c")
        s.raw_detections = Path("q")
        s.gff_result = Path("h.gff")
        s.mols_used_in_aligned_ccs = set(range(1000, 1118))
        s.aligned_ccs_bam_files = self.all_aligned_ccs_bam_files
        self.assertEqual(
            s.as_html,
            SUMMARY_REPORT_HTML_TEMPLATE.format(
                **self.expected_data_no_problems)
        )

    def test_molecule_sets_updated_by_MolsSetAttributes(
            self, pBamFile, prolling, pmultihist, pbars, phist, pd):
        with patch("pacbio_data_processing.summary.Path"):
            sr = SummaryReport("my.bam", "pbmm2.my.bam", self.reference)
        self.assertEqual(sr._molecule_sets["mols_dna_mismatches"], set())
        self.assertEqual(sr._molecule_sets["filtered_out_mols"], set())
        self.assertEqual(sr._molecule_sets["faulty_mols"], set())
        self.assertEqual(sr._molecule_sets["mols_used_in_aligned_ccs"], set())
        sr.mols_dna_mismatches = {17, 144}
        sr.filtered_out_mols = {1, 4, 6}
        sr.faulty_mols = {368}
        sr.mols_used_in_aligned_ccs = {3, 7}
        self.assertEqual(sr._molecule_sets["mols_dna_mismatches"], {17, 144})
        self.assertEqual(sr._molecule_sets["filtered_out_mols"], {1, 4, 6})
        self.assertEqual(sr._molecule_sets["faulty_mols"], {368})
        self.assertEqual(sr._molecule_sets["mols_used_in_aligned_ccs"], {3, 7})

    def test_molecule_sets_can_be_pickled(
            self, pBamFile, prolling, pmultihist, pbars, phist, pd):
        with patch("pacbio_data_processing.summary.Path"):
            sr = SummaryReport("my.bam", "pbmm2.my.bam", self.reference)
        mopen = mock_open()
        with patch("pacbio_data_processing.summary.pickle") as ppickle:
            with patch("pacbio_data_processing.summary.open", mopen):
                sr.dump_molecule_sets("whatnot.pickle")
        mopen.assert_called_once_with("whatnot.pickle", "wb")
        ppickle.dump.assert_called_once_with(
            sr._molecule_sets,
            mopen.return_value.__enter__.return_value,
            protocol=4
        )

    def test_molecule_sets_can_be_unpickled(
            self, pBamFile, prolling, pmultihist, pbars, phist, pd):
        with patch("pacbio_data_processing.summary.Path"):
            sr = SummaryReport("my.bam", "pbmm2.my.bam", self.reference)
        mopen = mock_open()
        with patch("pacbio_data_processing.summary.pickle") as ppickle:
            ppickle.load.return_value = {
                "mols_dna_mismatches": {1},
                "filtered_out_mols": {2, 3},
                "faulty_mols": {4},
                "mols_used_in_aligned_ccs": {6, 7, 8},
            }
            with patch("pacbio_data_processing.summary.open", mopen):
                sr.load_molecule_sets("whatnot.pickle")
        mopen.assert_called_once_with("whatnot.pickle", "rb")
        ppickle.load.assert_called_once_with(
            mopen.return_value.__enter__.return_value
        )
        self.assertEqual(sr._molecule_sets["mols_dna_mismatches"], {1})
        self.assertEqual(sr._molecule_sets["filtered_out_mols"], {2, 3})
        self.assertEqual(sr._molecule_sets["faulty_mols"], {4})
        self.assertEqual(
            sr._molecule_sets["mols_used_in_aligned_ccs"], {6, 7, 8})
        self.assertEqual(
            sr._loaded_molecule_sets,
            {"mols_dna_mismatches", "filtered_out_mols", "faulty_mols",
             "mols_used_in_aligned_ccs"}
        )

    def test_unpickled_molecule_sets_update_previous_values(
            self, pBamFile, prolling, pmultihist, pbars, phist, pd):
        with patch("pacbio_data_processing.summary.Path"):
            sr = SummaryReport("my.bam", "pbmm2.my.bam", self.reference)
        sr.mols_dna_mismatches = {17, 144}
        sr.filtered_out_mols = {1, 4, 6}
        sr.faulty_mols = {368}
        sr.mols_used_in_aligned_ccs = {3, 7}
        mopen = mock_open()
        with patch("pacbio_data_processing.summary.pickle") as ppickle:
            ppickle.load.return_value = {
                "mols_dna_mismatches": {10},
                "filtered_out_mols": {2, 30},
                "faulty_mols": {49},
                "mols_used_in_aligned_ccs": {60, 70, 80},
            }
            with patch("pacbio_data_processing.summary.open", mopen):
                sr.load_molecule_sets("whatnot.pickle")
        self.assertEqual(
            sr._molecule_sets["mols_dna_mismatches"], {17, 144, 10}
        )
        self.assertEqual(
            sr._molecule_sets["filtered_out_mols"], {1, 4, 6, 2, 30}
        )
        self.assertEqual(
            sr._molecule_sets["faulty_mols"], {368, 49}
        )
        self.assertEqual(
            sr._molecule_sets["mols_used_in_aligned_ccs"], {3, 7, 60, 70, 80}
        )

    def test_unpickling_molecule_sets_skips_missing_keys(
            self, pBamFile, prolling, pmultihist, pbars, phist, pd):
        with patch("pacbio_data_processing.summary.Path"):
            sr = SummaryReport("my.bam", "pbmm2.my.bam", self.reference)
        mopen = mock_open()
        with patch("pacbio_data_processing.summary.pickle") as ppickle:
            ppickle.load.return_value = {
                "mols_used_in_aligned_ccs": {60, 70, 80},
            }
            with patch("pacbio_data_processing.summary.open", mopen):
                sr.load_molecule_sets("whatnot.pickle")
        self.assertEqual(sr._molecule_sets["mols_dna_mismatches"], set())
        self.assertEqual(sr._molecule_sets["filtered_out_mols"], set())
        self.assertEqual(sr._molecule_sets["faulty_mols"], set())
        self.assertEqual(
            sr._molecule_sets["mols_used_in_aligned_ccs"], {60, 70, 80}
        )

    def test_multiple_loaded_mol_sets_are_kept(
            self, pBamFile, prolling, pmultihist, pbars, phist, pd):
        with patch("pacbio_data_processing.summary.Path"):
            sr = SummaryReport("my.bam", "pbmm2.my.bam", self.reference)
        mopen = mock_open()
        with patch("pacbio_data_processing.summary.pickle") as ppickle:
            ppickle.load.return_value = {
                "mols_used_in_aligned_ccs": {60, 70, 80},
            }
            with patch("pacbio_data_processing.summary.open", mopen):
                sr.load_molecule_sets("whatnot1.pickle")
            ppickle.load.return_value = {
                "filtered_out_mols": {3},
            }
            with patch("pacbio_data_processing.summary.open", mopen):
                sr.load_molecule_sets("whatnot2.pickle")
            ppickle.load.return_value = {
                "faulty_mols": set(),
            }
            with patch("pacbio_data_processing.summary.open", mopen):
                sr.load_molecule_sets("whatnot3.pickle")
        self.assertEqual(
            sr._loaded_molecule_sets,
            {"mols_used_in_aligned_ccs", "filtered_out_mols", "faulty_mols"}
        )

    def test__pre_save(
            self, pBamFile, prolling, pmultihist, pbars, phist, pd):
        s = self.create_summary_report(pBamFile)
        s._loaded_molecule_sets = {"one", "two"}
        s._molecule_sets = {"one": {1}, "two": {2}}
        with patch("pacbio_data_processing.summary.setattr") as psetattr:
            s._pre_save()
        psetattr.assert_has_calls(
            [call(s, "one", {1}), call(s, "two", {2})], any_order=True
        )


class MyBarsPlot(BarsPlotAttribute):
    title = "I see your wonders"
    dependency_names = (
        "what_a",
        "how_k"
    )
    data_definition = {
        'Bases covered': ("perc",),
        'Bases NOT covered': ("perc_not",),
    }
    index_labels = ("Points",)


class FakeHost4BarPlots:
    myplot = MyBarsPlot()
    perc = "2.03"
    perc_not = "3.76"

    def ready_to_go(self, *dependencies):
        return self._ready_to_go


@patch("pacbio_data_processing.summary.pandas")
class BarsPlotAttributeTestCase(unittest.TestCase):
    def test_get_if_not_ready(self, pd):
        host = FakeHost4BarPlots()
        host._ready_to_go = False
        self.assertIs(host.myplot, None)

    def test_get_if_ready(self, pd):
        host = FakeHost4BarPlots()
        host._ready_to_go = True
        host._data = {
            "myplot": "wonderf.png"
        }
        self.assertEqual(
            host.myplot,
            (pd.DataFrame.return_value, "I see your wonders", "wonderf.png")
        )
        pd.DataFrame.assert_called_once_with(
            {"Bases covered": [2.03], "Bases NOT covered": [3.76]},
            index=("Points",)
        )

    def test_issue83(self, pd):
        """It does not raise ValueError if a value is not float"""
        host = FakeHost4BarPlots()
        host.perc = "N/A"
        host._ready_to_go = True
        host._data = {
            "myplot": "wonderf.png"
        }
        host.myplot


class MyHistogramPlot(HistoryPlotAttribute):
    title = "A Beautiful Title"
    dependency_name = "wreck"
    column_name = "len(molecule)"
    data_name = "height"
    labels = ("Width",)
    legend = True
    # column = "obs"
    # hue = "src"


fake_make_data_for_plot = MagicMock()


class MyHistogramPlotDataFaked(MyHistogramPlot):
    make_data_for_plot = fake_make_data_for_plot


class MyPositionCoverageHistory(MyHistogramPlot, PositionCoverageHistory):
    ...


class MyMoleculeLenHistogram(MyHistogramPlot, MoleculeLenHistogram):
    labels = ("one label", "another label")


class MyMappingQualityHistogram(MyHistogramPlot, MappingQualityHistogram):
    dependency_name = "aligned_bam"


class FakeHost4Histograms:
    myhist = MyHistogramPlotDataFaked()
    myposhist = MyPositionCoverageHistory()
    mylenhist = MyMoleculeLenHistogram()
    mymapqhist = MyMappingQualityHistogram()
    bam = [["x"]*9+["x"*_] for _ in range(2, 10, 2)]
    reference_base_pairs = 23

    def ready_to_go(self, *dependencies):
        return self._ready_to_go


@patch("pacbio_data_processing.summary.pandas")
class HistogramPlotTestCase(unittest.TestCase):
    def test_get_if_not_ready(self, pd):
        host = FakeHost4Histograms()
        host._ready_to_go = False
        self.assertIs(host.myhist, None)

    def test_get_if_ready(self, pd):
        host = FakeHost4Histograms()
        host._ready_to_go = True
        host._data = {
            "myhist": "aggderf.png"
        }
        self.assertEqual(
            host.myhist,
            (fake_make_data_for_plot.return_value, "A Beautiful Title",
             "aggderf.png", True)
        )


@patch("pacbio_data_processing.summary.pandas")
class MappingQualityHistogramTestCase(unittest.TestCase):
    def test_get_if_not_ready(self, pd):
        host = FakeHost4Histograms()
        host._ready_to_go = False
        self.assertIs(host.mymapqhist, None)

    def test_get_if_ready(self, pd):
        host = FakeHost4Histograms()
        host._ready_to_go = True
        host._data = {
            "mymapqhist": "mqh.png"
        }
        host.aligned_bam = MagicMock()
        host.mapping_quality_threshold = 25
        pd.Series.return_value = (8, 12, 1, 23)
        expected_data = pd.Series.return_value
        self.assertEqual(
            host.mymapqhist,
            (expected_data, "A Beautiful Title", "mqh.png",
             True, 24, (False, True), 25, "mapping quality threshold")
        )

    def test_get_if_ready_but_no_threshold(self, pd):
        host = FakeHost4Histograms()
        host._ready_to_go = True
        host._data = {
            "mymapqhist": "mqh.png"
        }
        host.aligned_bam = MagicMock()
        pd.Series.return_value = (8, 12, 1, 23)
        expected_data = pd.Series.return_value
        self.assertEqual(
            host.mymapqhist,
            (expected_data, "A Beautiful Title", "mqh.png",
             True, 24, (False, True), None, "mapping quality threshold")
        )


@patch("pacbio_data_processing.summary.pandas")
class PositionCoverageHistoryTestCase(unittest.TestCase):
    def test_make_data_for_plot(self, pd):
        host = FakeHost4Histograms()
        host._ready_to_go = True
        host._data = {
            "myposhist": "aggderf.png",
            "wreck": "mr.csv",
        }
        raw_data = {
            "start of molecule": [1, 3, 15, 11, 20],
            "len(molecule)": [5, 2, 2, 5, 5],
        }
        expected_dict = {i: 0 for i in range(1, 23)}
        expected_dict.update(
            {
                1: 2, 2: 1, 3: 2, 4: 2, 5: 1,
                11: 1, 12: 1, 13: 1, 14: 1, 15: 2,
                16: 1, 20: 1, 21: 1, 22: 1, 23: 1
            }
        )
        pd.read_csv.return_value = raw_data
        plot_data = host.myposhist
        pd.read_csv.assert_called_once_with("mr.csv", delimiter=";")
        self.assertEqual(plot_data[0], expected_dict)


@patch("pacbio_data_processing.summary.pandas")
class MoleculeLenHistogramTestCase(unittest.TestCase):
    def test_make_data_for_plot(self, pd):
        host = FakeHost4Histograms()
        host._ready_to_go = True
        host._data = {
            "mylenhist": "aggderf.png",
        }
        host.wreck = "mr.csv"
        subreads = MagicMock()
        mols = MagicMock()
        pd.Series.return_value = subreads
        pd.read_csv.return_value.__getitem__.return_value = mols
        host.mylenhist
        pd.read_csv.assert_called_once_with("mr.csv", delimiter=";")
        pd.Series.assert_called_once_with(list(range(2, 10, 2)), name="height")
        self.assertEqual(mols.name, "height")


class MoleculeTypeBarsPlotTestCase(unittest.TestCase):
    def test_dependencies(self):
        # These two are needed, the rest have defaults:
        needed_attrs = (
            "mols_used_in_aligned_ccs", "methylation_report"
        )
        for attr in needed_attrs:
            self.assertIn(attr, MoleculeTypeBarsPlot.dependency_names)

    def test_data_definition(self):
        needed_columns = {
            "Used in aligned CCS": (
                "perc_mols_used_in_aligned_ccs",
                "perc_subreads_used_in_aligned_ccs"
            ),
            "Mismatch discards": (
                "perc_mols_dna_mismatches",
                "perc_subreads_dna_mismatches"
            ),
            "Filtered out": (
                "perc_filtered_out_mols",
                "perc_filtered_out_subreads"
            ),
            "Faulty (with processing error)": (
                "perc_faulty_mols",
                "perc_faulty_subreads"
            ),
            "In Methylation report with GATC": (
                "perc_mols_in_meth_report_with_gatcs",
                "perc_subreads_in_meth_report_with_gatcs"
            ),
            "In Methylation report without GATC": (
                "perc_mols_in_meth_report_without_gatcs",
                "perc_subreads_in_meth_report_without_gatcs"
            ),
        }
        for column, attrs in needed_columns.items():
            self.assertEqual(
                MoleculeTypeBarsPlot.data_definition[column], attrs
            )


class AttributesTestCase(unittest.TestCase):
    def setUp(self):
        class MyClass:
            _data = {
                "amount": 17.2,
                "total": 47,
            }
            perc_amount = PercAttribute(total_attr="total")
            reference = InputReferenceAttribute()
            _on = defaultdict(bool)

            def switch_on(self, attr):
                self._on[attr] = True

        self.instance = MyClass()

    def test_perc_attribute(self):
        self.assertEqual(self.instance.perc_amount, "36.60")

    def test_issue65(self):
        self.instance._data["total"] = 0
        self.assertEqual(self.instance.perc_amount, "N/A")

    def test_input_reference_attribute(self):
        class Reference:
            fasta_name = "mol.fasta"
            description = "No fun here\r\n"
            md5sum = "a3"
            _seq = "agtGaTcCGATC"

            def __len__(self):
                return len(self._seq)

            def upper(self):
                return self._seq.upper()

        self.instance.reference = Reference()
        self.assertEqual(self.instance.reference, "mol.fasta")
        self.assertEqual(self.instance._data["reference_name"], "No fun here")
        self.assertEqual(self.instance._data["reference_base_pairs"], 12)
        self.assertEqual(self.instance._data["reference_md5sum"], "a3")
        self.assertEqual(self.instance._data["total_gatcs_in_ref"], 2)
        self.assertTrue(self.instance._on["reference"])


class AlignedBamAttributeTestCase(unittest.TestCase):
    @patch("pacbio_data_processing.summary.BamFile")
    def test_sets_aligned_bam_attribute(self, pBamFile):
        class A:
            aligned_bam = AlignedBamAttribute()
            mapping_quality_threshold = 23

            def __init__(self):
                self._data = {}

            def switch_on(self, param):
                ...

        a = A()
        a.aligned_bam = "/dev/zero"

        self.assertEqual(a.aligned_bam, pBamFile.return_value)
        pBamFile.assert_called_once_with("/dev/zero")


class MappingQualityThresholdAttributeTestCase(unittest.TestCase):
    @patch("pacbio_data_processing.summary.BamFile")
    def test_sets_some_data_in_instance(self, pBamFile):
        class A:
            mapping_quality_threshold = MappingQualityThresholdAttribute()
            mapping_qualities = Series([3, 5, 7, 8, 4, 5, 23])

            def __init__(self):
                self._data = {}

            def switch_on(self, param):
                ...

        a = A()
        a.mapping_quality_threshold = 5

        self.assertEqual(a.mapping_quality_threshold, 5)
        self.assertEqual(a._data["subreads_with_low_mapq"], 2)
        self.assertEqual(a._data["subreads_with_high_mapq"], 5)

        a.mapping_quality_threshold = 6

        self.assertEqual(a.mapping_quality_threshold, 6)
        self.assertEqual(a._data["subreads_with_low_mapq"], 4)
        self.assertEqual(a._data["subreads_with_high_mapq"], 3)
