#! /usr/bin/env python
from __future__ import print_function

import sys

import numpy as np
import pandas


def read_data_chunk(path, start=0, nrows=5000):
    header = pandas.read_table(path, nrows=0)
    data = pandas.read_table(path, skiprows=start + 1,
                             nrows=nrows, names=header.columns)
    return data


def expand_range(range_str):
    try:
        low, high = range_str.split('-')
    except ValueError:
        return [int(range_str)]
    else:
        return range(int(low), int(high) + 1)


def parse_range_string(ranges):
    all_ints = []
    for range in ranges.split(','):
        all_ints += expand_range(range)

    return all_ints


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=argparse.FileType('r'),
                        default=sys.stdin, help='Text data file')
    parser.add_argument('rows', nargs='*', help='Rows to flag')
    parser.add_argument('--flag', help='Flag to add')

    args = parser.parse_args()

    data = pandas.read_table(args.data)

    if args.rows:
        rows = parse_range_string(','.join(args.rows))
        data.loc[rows, 'flags'] = args.flag
    else:
        data.loc[:, 'flags'] = args.flag

    data.to_csv(sys.stdout, sep='\t', index=False)


if __name__ == '__main__':
    main()