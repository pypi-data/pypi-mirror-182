#!/usr/bin/env python

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

"""Template to create a fake version of 'ipdSummary', expected to be
called like::

   ipdSummary  blasr.pMA683.subreads.476.bam --reference pMA683.fa \
   --identify m6A --gff basemods_pMA683.gff

and it must produce a file like: blasr.pMA683.subreads.476.bam.gff

"""

import sys
import shutil
from pathlib import Path, PosixPath  # noqa: F401
import time
from concurrent.futures import ProcessPoolExecutor
import logging
import os


MISSING_IDX = (
    "Companion FASTA index (.fai) file not found or malformatted! Use "
    "'samtools faidx' to generate FASTA index."
)
datadir = _DATA_DIR_  # noqa: F821
resources_dir = _RESOURCES_DIR_  # noqa: F821


bam2gff = {
    "m6A": {
        'pbmm2.11mols.19399571.bam': datadir/'pbmm2.11mols.19399571.gff',
        'pbmm2.11mols.23658875.bam': datadir/'pbmm2.11mols.23658875.gff',
        'pbmm2.11mols.28836053.bam': datadir/'pbmm2.11mols.28836053.gff',
        'pbmm2.11mols.29229724.bam': datadir/'pbmm2.11mols.29229724.gff',
        'pbmm2.11mols.45744686.bam': datadir/'pbmm2.11mols.45744686.gff',
        'pbmm2.11mols.52167204.bam': datadir/'pbmm2.11mols.52167204.gff',
        'pbmm2.11mols.55116046.bam': datadir/'pbmm2.11mols.55116046.gff',
        'pbmm2.11mols.59179888.bam': datadir/'pbmm2.11mols.59179888.gff',
        'pbmm2.11mols.60359568.bam': datadir/'pbmm2.11mols.60359568.gff',
        'pbmm2.11mols.72352689.bam': datadir/'pbmm2.11mols.72352689.gff',
        'pbmm2.11mols.74515099.bam': datadir/'pbmm2.11mols.74515099.gff',
        'pbmm2.8mols.25294.bam': datadir/'pbmm2.8mols.25294.bam.gff',
        'pbmm2.8mols.150700.bam': datadir/'pbmm2.8mols.150700.bam.gff',
        'pbmm2.8mols.14728.bam': datadir/'pbmm2.8mols.14728.bam.gff',
        'pbmm2.8mols.107947.bam': datadir/'pbmm2.8mols.107947.bam.gff',
        'pbmm2.8mols.67334.bam': datadir/'pbmm2.8mols.67334.bam.gff',
        'pbmm2.8mols.49610.bam': datadir/'pbmm2.8mols.49610.bam.gff',
        'pbmm2.8mols.89194.bam': datadir/'pbmm2.8mols.89194.bam.gff',
        'pbmm2.8mols.86474.bam': datadir/'pbmm2.8mols.86474.bam.gff',
        'pbmm2.12mols.23658875.bam': datadir/'pbmm2.12mols.23658875.bam.gff',
        'pbmm2.12mols.28836053.bam': datadir/'pbmm2.12mols.28836053.bam.gff',
        'pbmm2.12mols.29229724.bam': datadir/'pbmm2.12mols.29229724.bam.gff',
        'pbmm2.12mols.45744686.bam': datadir/'pbmm2.12mols.45744686.bam.gff',
        'pbmm2.12mols.52167204.bam': datadir/'pbmm2.12mols.52167204.bam.gff',
        'pbmm2.12mols.55116046.bam': datadir/'pbmm2.12mols.55116046.bam.gff',
        'pbmm2.12mols.59179888.bam': datadir/'pbmm2.12mols.59179888.bam.gff',
        'pbmm2.12mols.60359568.bam': datadir/'pbmm2.12mols.60359568.bam.gff',
        'pbmm2.12mols.72352689.bam': datadir/'pbmm2.12mols.72352689.bam.gff',
        'pbmm2.12mols.74515099.bam': datadir/'pbmm2.12mols.74515099.bam.gff',
        'pbmm2.12mols.9900000.bam': datadir/'pbmm2.12mols.9900000.bam.gff',
        'pbmm2.baseline.19399571.bam': datadir/'pbmm2.baseline.19399571.gff',
        'pbmm2.baseline.23658875.bam': datadir/'pbmm2.baseline.23658875.gff',
        'pbmm2.baseline.28836053.bam': datadir/'pbmm2.baseline.28836053.gff',
        'pbmm2.baseline.29229724.bam': datadir/'pbmm2.baseline.29229724.gff',
        'pbmm2.baseline.45744686.bam': datadir/'pbmm2.baseline.45744686.gff',
        'pbmm2.baseline.52167204.bam': datadir/'pbmm2.baseline.52167204.gff',
        'pbmm2.baseline.55116046.bam': datadir/'pbmm2.baseline.55116046.gff',
        'pbmm2.baseline.59179888.bam': datadir/'pbmm2.baseline.59179888.gff',
        'pbmm2.baseline.60359568.bam': datadir/'pbmm2.baseline.60359568.gff',
        'pbmm2.baseline.72352689.bam': datadir/'pbmm2.baseline.72352689.gff',
        'pbmm2.baseline.74515099.bam': datadir/'pbmm2.baseline.74515099.gff',
        'pbmm2.9mols.150700.bam': datadir/'pbmm2.9mols.150700.gff',
        'pbmm2.9mols.107947.bam': datadir/'pbmm2.9mols.107947.gff',
        'pbmm2.9mols.67334.bam': datadir/'pbmm2.9mols.67334.gff',
        'pi-shifted.pbmm2.9mols.155993.bam':
        datadir/'pi-shifted.pbmm2.9mols.155993.gff',
    },
    "m4C,m6A": {
        'pbmm2.11mols.19399571.bam': datadir/'pbmm2.11mols.19399571.bam.gff_m6A-m4C',
        'pbmm2.11mols.23658875.bam': datadir/'pbmm2.11mols.23658875.bam.gff_m6A-m4C',
        'pbmm2.11mols.28836053.bam': datadir/'pbmm2.11mols.28836053.bam.gff_m6A-m4C',
        'pbmm2.11mols.29229724.bam': datadir/'pbmm2.11mols.29229724.bam.gff_m6A-m4C',
        'pbmm2.11mols.45744686.bam': datadir/'pbmm2.11mols.45744686.bam.gff_m6A-m4C',
        'pbmm2.11mols.52167204.bam': datadir/'pbmm2.11mols.52167204.bam.gff_m6A-m4C',
        'pbmm2.11mols.55116046.bam': datadir/'pbmm2.11mols.55116046.bam.gff_m6A-m4C',
        'pbmm2.11mols.59179888.bam': datadir/'pbmm2.11mols.59179888.bam.gff_m6A-m4C',
        'pbmm2.11mols.60359568.bam': datadir/'pbmm2.11mols.60359568.bam.gff_m6A-m4C',
        'pbmm2.11mols.72352689.bam': datadir/'pbmm2.11mols.72352689.bam.gff_m6A-m4C',
        'pbmm2.11mols.74515099.bam': datadir/'pbmm2.11mols.74515099.bam.gff_m6A-m4C',
        'pbmm2.8mols.25294.bam': datadir/'pbmm2.8mols.25294.bam.gff_m6A-m4C',
        'pbmm2.8mols.150700.bam': datadir/'pbmm2.8mols.150700.bam.gff_m6A-m4C',
        'pbmm2.8mols.14728.bam': datadir/'pbmm2.8mols.14728.bam.gff_m6A-m4C',
        'pbmm2.8mols.107947.bam': datadir/'pbmm2.8mols.107947.bam.gff_m6A-m4C',
        'pbmm2.8mols.67334.bam': datadir/'pbmm2.8mols.67334.bam.gff_m6A-m4C',
        'pbmm2.8mols.49610.bam': datadir/'pbmm2.8mols.49610.bam.gff_m6A-m4C',
        'pbmm2.8mols.89194.bam': datadir/'pbmm2.8mols.89194.bam.gff_m6A-m4C',
        'pbmm2.8mols.86474.bam': datadir/'pbmm2.8mols.86474.bam.gff_m6A-m4C',
    }
}


def heavy_lifting():
    # To allow the FTs to detect the processes:
    # the sleep time must be >~ 0.2 to allow the process hunter function
    # "count_nprocs" to have a chance to find this process:
    pid = os.getpid()
    markerfile = Path(f".ipdSummary.pid.{pid}")
    markerfile.touch()
    time.sleep(0.3)


def check_needed_files(bam: Path) -> None:
    """The ipdSummary program must fail if either the input BAM or the
    companion pbi file is missing.
    This function makes sure of that.
    """
    bam_is_there = bam.is_file()
    pbi = bam.with_suffix(".bam.pbi")
    pbi_is_there = pbi.is_file()
    if bam_is_there and pbi_is_there:
        return
    else:
        logging.error(
            "[root monitorChildProcesses xxx] Child process exited with"
            " exitcode=1.  Aborting."
        )
        sys.exit(1)


def main(nprocs):
    if nprocs == 1:
        heavy_lifting()
    else:
        with ProcessPoolExecutor(max_workers=nprocs) as executor:
            for i in range(nprocs):
                executor.submit(heavy_lifting)


if __name__ == "__main__":
    modification_types = "m6A"
    bam = Path(sys.argv[1])
    num_workers = 1

    for i, arg in enumerate(sys.argv):
        if arg == "--gff":
            outfile = Path(sys.argv[i+1])
            wdir = outfile.parent
        elif arg == "--identify":
            modification_types = ",".join(sorted(sys.argv[i+1].split(",")))
        elif arg == "--reference":
            reference = Path(sys.argv[i+1])
            assert reference.exists()
            open(reference).close()  # check that is readable
            reference_idx = reference.with_name(reference.name+".fai")
            if not reference_idx.exists():
                raise OSError(MISSING_IDX)
        elif arg == "--ipdModel":
            model = Path(sys.argv[i+1])
            assert model.is_file()
        elif arg in ("--numWorkers", "-j"):
            num_workers = int(sys.argv[i+1])

    if _EXIT_CODE_ == 0:  # noqa: F821
        for failing_mol in _FAILING_MOLS_:  # noqa: F821
            if failing_mol in bam.name:
                print("whatever I feel like I wanna do", file=sys.stderr)
                sys.exit(1)
        check_needed_files(bam)
        main(num_workers)
        bam_key = bam.name
        if bam_key.startswith("blasr"):
            bam_key = bam_key.replace("blasr", "pbmm2")
        bam_dict = bam2gff[modification_types]
        shutil.copyfile(bam_dict[bam_key], outfile)
    sys.exit(_EXIT_CODE_)  # noqa: F821
