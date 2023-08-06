#######################################################################
#
# Copyright (C) 2022 David Velázquez
# Copyright (C) 2022 David Palao
#
# This file is part of PacBio data processing.
#
#  PacBioDataProcessing is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  PacBio data processing is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with PacBioDataProcessing. If not, see <http://www.gnu.org/licenses/>.
#
#######################################################################

from typing import Union, NewType, Optional
from pathlib import Path
from collections import defaultdict

from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
from pandas import DataFrame, Series


sns.set_theme()

Position = NewType("Position", int)
Coverage = NewType("Coverage", int)
Bins = NewType("Bins", int)


def make_barsplot(
        dataframe: DataFrame,
        plot_title: str,
        filename: Union[Path, str]
        ) -> None:
    f, ax = plt.subplots(figsize=(10, 5))
    dataframe.plot.bar(rot=0, ax=ax)
    for p in ax.patches:
        ax.annotate(
            p.get_height(),
            (p.get_x() + p.get_width() / 2., p.get_height()),
            ha='center', va='center',
            fontsize=10, weight='bold', color='black', xytext=(0, 5),
            textcoords='offset points'
        )
    ax.set_title(plot_title, fontsize=12, weight='bold')

    # Put a legend to the right of the current axis
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close(f)


def make_histogram(
        series: Series,
        plot_title: str,
        filename: Union[Path, str],
        legend: bool = True,
        bins: Optional[int] = None,
        log_scale: Optional[tuple] = None,
        vertical_line_at: Optional[float] = None,
        vertical_line_label: Optional[str] = None,
        ) -> None:
    f, ax = plt.subplots(figsize=(8, 5))

    more_kwds = {}
    if bins:
        more_kwds["bins"] = bins
    if log_scale:
        more_kwds["log_scale"] = log_scale

    sns.histplot(data=series, ax=ax, **more_kwds)

    if vertical_line_at:
        axvline_dict = {"color": "darkgreen"}
        if vertical_line_label:
            axvline_dict["label"] = (
                f"{vertical_line_label} (at {vertical_line_at})"
            )
        ax.axvline(vertical_line_at, **axvline_dict)

    if False:  # Untested and not nedded, hence disabled.
        min_value = series.min()
        mean_value = np.round(series.mean(), 3)
        max_value = series.max()
        ax.axvline(min_value, label=f'Min value: {min_value}', color='green')
        ax.axvline(
            mean_value, label=f'Mean value: {mean_value}', color='royalblue')
        ax.axvline(
            max_value, label=f'Max value: {max_value}', color='orangered')

    ax.set_title(plot_title, fontsize=12, weight='bold')

    if legend:
        ax.legend()

    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close(f)


def make_multi_histogram(
        data: dict[str, Series],
        plot_title: str,
        filename: Union[Path, str],
        legend: bool = True
        ) -> None:
    f, ax = plt.subplots(figsize=(15, 5))
    # colors = ["royalblue", "orange", "seagreen", "orchid", "maroon"]
    colors = sns.color_palette("tab10")
    for color, (label, serie) in zip(colors, data.items()):
        mean_value = serie.mean()
        label_with_mean = f"{label} (mean length: {mean_value:.0f})"
        plot = sns.histplot(
            data=serie,
            # x=column, #"length",
            # hue=hue, #"source",
            label=label_with_mean,
            stat="percent",
            ax=ax,
            kde=True,
            color=color,
            log_scale=(True, False)
        )
        plot.tick_params(labelsize=12)
        plot.set_xlabel(xlabel=serie.name, fontsize=18)
        plot.set_ylabel(ylabel="Percent", fontsize=18)
    ax.set_title(plot_title, fontsize=18, weight='bold')
    ax.tick_params(axis='both', which='major', labelsize=18)
    # plt.xticks(fontsize=18)
    if legend:
        ax.legend(fontsize=16)
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close(f)


def make_continuous_rolled_data(
        data: dict[Position, Coverage], window: int) -> DataFrame:
    """Auxiliary function used by ``make_rolling_history`` to produce
    a dataframe with the rolling average of the input data.
    The resulting dataframe starts at the min input position and ends
    at the max input position. The holes are set to 0 in the input
    data.
    """
    N = max(data.keys())
    k0 = min(data.keys())
    data = defaultdict(int, data)
    for i in range(window):
        data[k0-1-i] = data[N-i]
        data[N+i+1] = data[i+k0]
    coverage = Series(data)
    positions = list(range(k0-window, N+1+window))
    df = DataFrame(
        {"positions": positions, "coverage": coverage},
        index=positions
    )
    rolled = df.rolling(window, on="positions", center=True)
    rolled_df = rolled.mean().fillna(0)
    rolled_df.index.name = "positions"
    return rolled_df[window:N+window+1-k0]


def make_rolling_history(
        data: dict[Position, Coverage],
        plot_title: str,
        filename: Union[Path, str],
        legend: bool = True,
        window: int = 1000
        ) -> None:
    # Should make it from a Series object?
    rolled_df_data = make_continuous_rolled_data(data, window)
    f, ax = plt.subplots(figsize=(15, 5))
    # In the next call, ``estimator=None`` makes the plot way faster
    # avoiding unnecessary computations of any error estimator.
    # With seaborn-0.11.2 it used to be ``ci=None``. Have a look at
    # https://stackoverflow.com/questions/56170909
    # to understand what was the reson for that.
    # BUT With seaborn-0.12.0 there was a performance regression and
    # a deprecation using ``ci=None``.
    # ``estimator=None`` is the way to go:
    # - to avoid the performance regression,
    # - to remove some DepreacationWarning's in the tests,
    # - to use the new API, and
    # - to make the code clearer.
    # See https://github.com/mwaskom/seaborn/issues/3006
    plot = sns.lineplot(
        data=rolled_df_data,
        x="positions", y="coverage",
        label=f"rolling average (window={window})",
        ax=ax, estimator=None
    )
    plot.tick_params(labelsize=12)
    plot.set_xlabel(xlabel="Position", fontsize=18)
    plot.set_ylabel(ylabel="Coverage", fontsize=18)
    ax.set_title(plot_title, fontsize=18, weight='bold')
    ax.tick_params(axis='both', which='major', labelsize=18)
    if legend:
        ax.legend(fontsize=16)
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close(f)
