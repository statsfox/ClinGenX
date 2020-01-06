# /usr/bin/env python
"""
ClinGenX: a tools designed to calculate clinicaally relevant metrics relating to NGS read coverage

"""

import os
import argparse
import logging
from Bedline import Bedline
from Depth import Depth
from Coverage import Coverage
from Gaps import Gaps

def collect_input_arguments():
    """
    collect command line arguments

    """

    # argparse object
    parser = argparse.ArgumentParser(
        description='ClinGenX: a tool designed to calculate clinicaally relevant metrics relating to NGS read coverage')

    # arguments
    parser.add_argument('--bedfile', required=True, help="path to bedfile", type=str)
    parser.add_argument('--depthfile', required=True, help='path to file containing read depth-per-bp', type=str)
    parser.add_argument('--padding', required=False, help='basepair padding value', default=0, type=int)
    parser.add_argument('--mindepth', required=False, help="coverage threshold", default=100, type=int)
    parser.add_argument('--outname', required=False, help="output file name", default="output", type=str)
    parser.add_argument('--config_path', required=False, help="path to yaml config file", type=str)

    # parse
    args = parser.parse_args()

    return args


def parse_config(config_path):
    """
    parse the YAML config file

    """

    with open(config_path, 'r') as stream:

        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            raise


def main():
    # collect command line args
    args = collect_input_arguments()

    # parse config file is defined
    try:
        config_dict = parse_config(config_path)
    except:
        print("no config file defined")

    # open bedfile
    with open(args.bedfile, "r") as bed:
        for ln in bed:
            chr = str(ln.split("\t")[0])
            start = int(ln.split("\t")[1])
            end = int(ln.split("\t")[2])

            # get bed object
            bedline = Bedline(chr, start, end)
            depth = Depth(depthfile=args.depthfile, bedline=bedline)
            coverage = Coverage(depth=depth, mindepth=args.mindepth)
            gaps = Gaps(depth=depth, mindepth=args.mindepth)

            print(bedline.chr.seq)
            print(bedline.start.coordinate)
            print(bedline.end.coordinate)
            print(coverage.avg_coverage)
            print(coverage.perc_mindepth)

            for rec in depth.records:
                print(rec)


if __name__ == '__main__':
    main()
