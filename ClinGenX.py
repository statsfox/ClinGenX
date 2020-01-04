#/usr/bin/env python
"""
ClinGenX: a tools designed to calculate clinicaally relevant metrics relating to NGS read coverage

"""

import os
import argparse
import logging
from Bedline import Bedline
import logging



def collect_input_arguments():
    """
    collects command line arguments

    """

    # argparse object
    parser = argparse.ArgumentParser(
        description='ClinGenX: a t   ools designed to calculate clinicaally relevant metrics relating to NGS read coverage')

    # arguments
    parser.add_argument('--bedfile', required=True, help="path to bedfile", type=str)
    parser.add_argument('--depthfile', required=True, help='path to file containing read depth-per-bp', type=str)
    parser.add_argument('--padding', required=False, help='basepair padding value', default=0, type=int)
    parser.add_argument('--depth', required=False, help="coverage threshold", default=100, type=int)
    parser.add_argument('--outname', required=False, help="output file name", default="output", type=str)

    # parse
    args = parser.parse_args()

    return args



def main():

    args = collect_input_arguments()

    # open bedfile
    with open(args.bedfile, "r") as bed:
        for ln in bed:

            chr = str(ln.split("\t")[0])
            start = int(ln.split("\t")[1])
            end = int(ln.split("\t")[2])

            # get bed object
            bedline=Bedline(chr,start,end)
            print(bedline.chr.seq)
            print(bedline.start.coordinate)
            print(bedline.end.coordinate)



if __name__ == '__main__':

	main()