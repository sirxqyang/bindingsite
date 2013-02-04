#! /usr/bin/env python
#+++++++++++++++++++++++++++++++++++++
# get hit region after motif scan
# Xiaoqin Yang @ Tongji University
#+++++++++++++++++++++++++++++++++++++

import re
from math import fabs
import sys
from optparse import OptionParser

def motifregion(input, output):

        f = open(input, 'r')
        o = open(output, 'w')
        for line in f:
                if re.search("^chr", line):
                        if re.search("\t\t", line):
                                parts = line.strip().split("\t")
                                peak = parts[0]
                                elements = peak.split(":")
                                chr = elements[0]
                                pieces = elements[1].split("-")
                                peakstart = int(pieces[0])
                                Line = elements[1]
                                point = int(parts[4])
                                seqlen = len(parts[5])
                                if point > 0:
                                        Start = str(point + peakstart) 
                                        End = str(point + seqlen + peakstart)
                                elif point < 0:
                                        point = int(fabs(point))
                                        Start = str(point - seqlen + peakstart)
                                        End = str(point + peakstart)
                                Line = chr + "\t" + Start + "\t" + End + "\n"
                                o.write(Line)
                        else:
                                pass
                else:
                        pass



# Standard boilerplate to call the main() function
# to begin the program.
if __name__ == '__main__':

        usage = 'usage: python wig_divide.py -i input -o output'
        parser = OptionParser(usage)
        parser.add_option("-i", "--input", dest="input", help="input results of motif scan")
        parser.add_option("-o", "--output", dest="output", help="bed file of motif region")

        (options, args) = parser.parse_args()

        if not options.input:   # only required argument
                parser.print_help()
                sys.exit(1)

        motifregion(options.input, options.output)
