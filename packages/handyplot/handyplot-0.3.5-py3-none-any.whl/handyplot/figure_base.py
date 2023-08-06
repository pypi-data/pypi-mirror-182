import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


class FigureBase:
    def __init__(self):
        mpl.rcParams["axes.autolimit_mode"] = "round_numbers"  # This expands the axis limits to the next round number.
        mpl.rcParams["font.family"] = ["Arial"]  # Set global font.
        mpl.rcParams["font.size"] = 10  # Set global font size.

        # plt means the canvas
        self._fig, self._axes = plt.subplots()
        # adjust figure padding margins
        plt.subplots_adjust(left=0.1, right=0.95, top=0.95, bottom=0.1)

    def add_text(self, x, y, text):
        plt.text(x, y, text)

    def save(self, filename, dpi=300):
        # self._fig.tight_layout()
        self._fig.savefig(filename, dpi=dpi)

    def set_canvas_margin(self, left=0.1, right=0.05, top=0.05, bottom=0.1):
        """
        :param left: wide percentage like 0.1
        :param right:
        :param top:
        :param bottom:
        :return:
        """

        plt.subplots_adjust(left=left, right=1-right, top=1-top, bottom=bottom)

    def set_title(self, title):
        self._axes.set_title(title)

    def set_xlabel(self, text):
        self._axes.set_xlabel(text)

    def set_xlimit(self, range, segment_num=None):
        self._axes.set_xlim(range)
        if segment_num is not None:
            self._axes.xaxis.set_ticks(np.linspace(range[0], range[1], segment_num+1))

    def set_ylabel(self, text):
        self._axes.set_ylabel(text)

    def set_ylimit(self, range, segment_num=None):
        self._axes.set_ylim(range)
        if segment_num is not None:
            self._axes.yaxis.set_ticks(np.linspace(range[0], range[1], segment_num+1))

    def show(self):
        # self._fig.tight_layout()
        self._fig.show()