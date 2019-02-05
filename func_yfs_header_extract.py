#!/usr/bin/env python

__version__ = "20181127"
__author__ = "Decaff_42"
__copyright__ = "2018 by Decaff_42"
__license__ = """Only non-commercial use with attribution is allowed without
prior written permission from Decaff_42."""


def BREAK():
    print("----------------------------------------------------")


def extract_yfs_header(data):
    """Extract key information from the YFS header"""
    ysf_version = ""
    scenery_name = ""
    event_block_start_line = 0

    for ind, line in enumerate(data):
        if line.startswith("YFSVERSI"):
            ysf_version = line.split(" ")[-1]
        elif line.startswith("FIELDNAM"):
            scenery_name = line.split(" ")[1]
        elif line.startswith("EVTBLOCK"):
            event_block_start_line = ind
            break

    print("YSF Version:  {}".format(ysf_version))
    print("Map:          {}".format(scenery_name))
    BREAK()

    return ysf_version, scenery_name