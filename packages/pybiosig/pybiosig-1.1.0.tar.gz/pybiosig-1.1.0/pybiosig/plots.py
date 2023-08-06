"""
-----------------------------------------------------------------------------------------
plots module
-----------------------------------------------------------------------------------------
Provides functions to visualize Signal class.

### Functions:

- iplot()     : Signal interactive plot for Notebooks.
- isubplot()  : Signal interactive subplot for Notebooks.

### Author: 

Alejandro Alcaine Otín, Ph.D.
    lalcaine@usj.es"""

# DEPENDENCIES

import numpy as np
from bokeh.plotting import figure
from bokeh.io import output_notebook, show
from bokeh.palettes import Colorblind
from bokeh.models import HoverTool
from bokeh.layouts import gridplot

from pybiosig.signal import Signal

# INTERACTIVE VISUALIZATIONS


def iplot(
    signal: Signal,
    x_lim: tuple = None,
    y_lim: tuple = None,
    fig_title: str = "",
    x_label: str = "Time (s)",
    y_label: str = "Amplitude (mV)",
    legend: list[str] = None,
    plot_width: int = 700,
    plot_height: int = 450,
    line_width: float = 1.5,
    to_notebook: bool = True,
) -> figure:
    """Signal interactive plot for Notebooks.

    Args:
        signal (Signal): Signal to visualize.

        x_lim (tuple, optional): Horizontal axis span limitation.
        Defaults to None: Time span of the signal/s.

        y_lim (tuple, optional): Vertical axis span limitation.
        Defaults to None: 105% of max/min amplitude of the signal/s.

        fig_title (str, optional): Title of the figure.
        Defaults to "".

        x_label (str, optional): Label for the horizontal axis.
        Defaults to "Time (s)".

        y_label (str, optional): Label for the vertical axis.
        Defaults to "Amplitude (mV)".

        legend (list[str], optional): Legend to be displayed (for multiple signals).
        Defaults to None: No legend is going to be displayed.

        plot_width (int, optional): Width of the plot.
        Defaults to 700.

        plot_height (int, optional): Height of the plot.
        Defaults to 450.

        line_width (float, optional): Width of the signal line.
        Defaults to 1.5.

        to_notebook (bool, optional): Output plot into notebook.
        Defaults to True.

    Returns:
        figure: Bokeh figure object if to_notebook = False.

        Returns -1 if any error happens
    """
    if to_notebook:
        output_notebook(hide_banner=True)

    t = signal.time_vector

    plot = figure(
        title=fig_title,
        x_axis_label=x_label,
        y_axis_label=y_label,
        x_range=(min(t), max(t)) if x_lim is None else x_lim,
        width=plot_width,
        height=plot_height,
        toolbar_location="below",
    )

    try:
        if legend is None:
            if y_lim is None:
                plot.y_range.update(start=signal.min() * 1.05, end=signal.max() * 1.05)
            else:
                plot.y_range.update(start=y_lim[0], end=y_lim[1])

            for i in range(signal.num_signals):
                plot.line(
                    t, signal[:, i], line_width=line_width, color=Colorblind[8][i % 8]
                )
        else:
            if y_lim is not None:
                plot.y_range.update(start=y_lim[0], end=y_lim[1])

            for i, leg in enumerate(legend):
                try:
                    # i = signal.channels.index(leg)
                    plot.line(
                        t,
                        signal[leg],
                        line_width=line_width,
                        color=Colorblind[8][i % 8],
                        legend_label=leg,
                    )
                    if y_lim is None:
                        plot.y_range.update(
                            start=plot.y_range.start
                            if plot.y_range.start < signal[:, leg].min()
                            else signal[:, leg].min() * 1.05,
                            end=plot.y_range.end
                            if plot.y_range.end > signal[:, leg].max()
                            else signal[:, leg].max() * 1.05,
                        )
                except IndexError:
                    print(f"WARNING: {leg} is not an available signal.")

            plot.legend.click_policy = "hide"

            plot.add_layout(plot.legend[0], "right")

        plot.add_tools(
            HoverTool(
                line_policy="nearest",
                point_policy="snap_to_data",
                tooltips=[(y_label, "$y{0.00}"), (x_label, "$x{0.00}")],
            )
        )

        show(plot, notebook_handle=to_notebook)

        if not to_notebook:
            return plot
    except Exception as error:
        print("Error:" + str(error))
        return -1


def isubplot(
    signal: Signal,
    x_lim: tuple = None,
    y_lim: tuple = None,
    sync_axis: bool = True,
    fig_title: list[str] = None,
    x_label: str = "Time (s)",
    y_label: str = "Amplitude (mV)",
    plot_width: int = 700,
    plot_height: int = 300,
    line_width: float = 1.5,
    to_notebook: bool = True,
) -> figure:
    """Signal interactive subplots for Notebooks.

    Args:
        signal (Signal): Signal to visualize.

        x_lim (tuple, optional): Horizontal axis span limitation.
        Defaults to None: Time span of the signal/s.

        y_lim (tuple, optional): Vertical axis span limitation.
        Defaults to None: Automatically handled by bokeh.

        sync_axis (bool, optional): Controls wether to sync or not axis among subplots.
        Defaults to True.

        fig_title (list[str], optional): Each subplot title.
        Defaults to None: Subplots are named "Signal 1", "Signal 2", ...

        x_label (str, optional): Label for the horizontal axis.
        Defaults to "Time (s)".

        y_label (str, optional): Label for the vertical axis.
        Defaults to "Amplitude (mV)".

        plot_width (int, optional): Width of the plot.
        Defaults to 700.

        plot_height (int, optional): Height of the plot.
        Defaults to 300.

        line_width (float, optional):  Width of the signal line.
        Defaults to 1.5.

        to_notebook (bool, optional): Output plot into notebook.
        Defaults to True.

    Returns:
        figure: Bokeh figure object if to_notebook = False.

        Returns -1 if any error happens
    """
    if to_notebook:
        output_notebook(hide_banner=True)

    t = signal.time_vector

    try:
        if fig_title is None:
            fig_title = [f"signal {i + 1:d}" for i in range(signal.num_signals)]

        plots = [
            figure(
                title=title,
                x_axis_label=x_label,
                y_axis_label=y_label,
                x_range=(min(t), max(t)) if x_lim is None else x_lim,
                width=plot_width,
                height=plot_height,
            )
            for title in fig_title
        ]

        for i, plot in enumerate(plots):
            try:
                plot.line(t, signal[fig_title[i]], line_width=line_width)
            except IndexError:
                plot.line(t, signal[:, i], line_width=line_width)

            if y_lim is not None and i == 0:
                plot.y_range.update(start=y_lim[0], end=y_lim[1])

            if i > 0 and sync_axis:  # This synchronizes all subplots for panning
                plot.x_range = plots[0].x_range
                plot.y_range = plots[0].y_range

            plot.add_tools(
                HoverTool(
                    line_policy="nearest",
                    point_policy="snap_to_data",
                    tooltips=[(y_label, "$y{0.00}"), (x_label, "$x{0.00}")],
                )
            )

        show(
            gridplot(children=plots, ncols=1, merge_tools=True),
            notebook_handle=to_notebook,
        )

        if not to_notebook:
            return plot
    except Exception as error:
        print("Error:" + str(error))
        return -1
