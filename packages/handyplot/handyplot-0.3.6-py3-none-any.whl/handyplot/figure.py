from handyplot.figure_base import FigureBase


class Figure(FigureBase):
    def __init__(self):
        FigureBase.__init__(self)

    def add_legend(self, loc="best", ncol=1, title=None, handles=None):
        """
        :param loc:
        a str descript the location:
            "best", "center", "upper left", "upper right", "lower left", "lower right", "upper center", "lower center",
            "center left"
        a coodinate:
            parameter range from 0~1, like (0.1, 0.1), (0.5, 0.7)
        :param ncol:
        :param title:
        :return:
        """
        self._axes.legend(loc=loc, ncol=ncol, title=title, handles=handles)

    def add_line(self, base, data, label=None, color=None):
        line, = self._axes.plot(base, data, color=color)

        if label is not None:
            line.set_label(label)

        return line

    def add_scatter(self, base, data, label=None, color=None, marker="o", markersize=None):
        if color is None:
            color = (0, 0, 0, 1)

        # line color is opacity in scatter
        scatter, = self._axes.plot(base, data, color=(0, 0, 0, 0), marker=marker, markeredgecolor=color,
                                   markersize=markersize)

        if label is not None:
            scatter.set_label(label)

        return scatter

    def open_grid(self):
        self._axes.grid(color=(235/255, 235/255, 235/255))
