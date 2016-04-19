#! /usr/bin/env python
from __future__ import print_function

import sys

import numpy as np
import pandas

from utils import dataframe_to_csv


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='Add a new column to a WAIS data set')
    parser.add_argument('--data', type=argparse.FileType('r'),
                        default=sys.stdin, help='Text data file')
    parser.add_argument('col', default='.', help='Name of the new column')
    parser.add_argument('--val', default='.',
                        help='Default value of the column')

    args = parser.parse_args()

    data = pandas.read_table(args.data)

    data.loc[:, args.col] = args.val
    dataframe_to_csv(data)


if __name__ == '__main__':
    main()
