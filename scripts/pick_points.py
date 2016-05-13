#! /usr/bin/env python
from __future__ import print_function

import sys

import numpy as np
import pandas
import matplotlib as mpl

mpl.use('Qt4Agg')

import matplotlib.pyplot as plt

from utils import read_data_chunk


VALID_FLAGS = ('P', 'S', 'N', 'O', 'V', 'F', )


class PointGetter(object):
    def __init__(self, file=None):
        self._file = file or sys.stdout
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)

        self.key_is_held = False

        self.fig.canvas.mpl_connect('pick_event', self.on_pick)
        self.fig.canvas.mpl_connect('key_press_event', self.on_key_press)
        self.fig.canvas.mpl_connect('key_release_event', self.on_key_release)

        self._picked = []

    def on_pick(self, event):
        if self.key_is_held:
            this_line = event.artist
            xdata, ydata = this_line.get_xdata(), this_line.get_ydata()
            ind = event.ind[0]
            self._picked.append(xdata[ind])
            if len(self._picked) == 2:
                self.print_range()

    def on_key_press(self, event):
        if event.key in VALID_FLAGS:
            self.key_is_held = event.key
        else:
            print(event.key)

    def on_key_release(self, event):
        if event.key in VALID_FLAGS:
            self.print_range()
            self.key_is_held = False

    def print_range(self):
        if len(self._picked) > 0:
            range = '{low:d}'.format(low=self._picked[0])
            if len(self._picked) > 1:
                range += '-{high:d}'.format(high=self._picked[1])
            print('{range} {flag}'.format(range=range, flag=self.key_is_held),
                  file=self._file)
        self._picked = []


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='Text data file')
    parser.add_argument('output', nargs='?', type=argparse.FileType('w'),
                        default=sys.stdout, help='Output file')
    parser.add_argument('--nrows', type=int, default=5000,
                        help='Number of rows to read')
    parser.add_argument('--start', type=int, default=0, help='Chunk to read')

    args = parser.parse_args()

    data = read_data_chunk(args.file, start=args.start, nrows=args.nrows)

    y = data.d18o
    x = np.arange(args.start, args.start + len(y))

    pg = PointGetter(file=args.output)
    pg.ax.plot(x, y, 'o', picker=5)
    pg.ax.set_title('Hold down a flag key to select points ({keys})'.format(
        keys=','.join(VALID_FLAGS)))

    plt.show()


if __name__ == '__main__':
    main()
