#!/usr/bin/env python

from __future__ import print_function

import argparse
import sys

def main(argv):
    parser = argparse.ArgumentParser(description='Build magnitude tests.')
    parser.parse_args(argv)

    # The test data file comes from the paper:
    # https://arxiv.org/pdf/1808.01973.pdf

    with open('Ap_Mag_Input_V3.txt') as f:
        lines = f.read().splitlines()

    print("""
from skyfield import magnitudelib as m""")

    for line in lines:
        if line.isupper():
            planet = line.lower()
            if planet not in ('mercury', 'venus'):
                break
            print('\ndef test_{}_magnitude_function():'.format(planet))
        elif line[0] == ' ' and line[1].isdigit():
            fields = line.split()
            if planet == 'mercury':
                args = fields[4], fields[6], fields[8]
            elif planet == 'venus':
                args = fields[4], fields[6], fields[10]
            answer = fields[-1]
            print('    assert abs({} - m.{}_magnitude({})) < 0.0005'
                  .format(answer, planet, ', '.join(str(arg) for arg in args)))

if __name__ == '__main__':
    main(sys.argv[1:])
