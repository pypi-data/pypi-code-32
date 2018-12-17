#!/usr/bin/env python
"""Collection of functions for the manipulation of time series."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import warnings

import mando
from mando.rst_text_formatter import RSTHelpFormatter
import pandas as pd

from .. import tsutils

warnings.filterwarnings('ignore')


@mando.command(formatter_class=RSTHelpFormatter, doctype='numpy')
@tsutils.doc(tsutils.docstrings)
def rolling_window(statistic=None,
                   groupby=None,
                   window=None,
                   input_ts='-',
                   columns=None,
                   start_date=None,
                   end_date=None,
                   dropna='no',
                   skiprows=None,
                   index_type='datetime',
                   names=None,
                   clean=False,
                   span=None,
                   min_periods=None,
                   center=False,
                   win_type=None,
                   on=None,
                   closed=None,
                   source_units=None,
                   target_units=None,
                   print_input=False):
    """Calculate a rolling window statistic.

    Parameters
    ----------
    statistic : str
        [optional, default is '']

        +----------+--------------------+
        | corr     | correlation        |
        +----------+--------------------+
        | count    | count of numbers   |
        +----------+--------------------+
        | cov      | covariance         |
        +----------+--------------------+
        | kurt     | kurtosis           |
        +----------+--------------------+
        | max      | maximum            |
        +----------+--------------------+
        | mean     | mean               |
        +----------+--------------------+
        | median   | median             |
        +----------+--------------------+
        | min      | minimum            |
        +----------+--------------------+
        | quantile | quantile           |
        +----------+--------------------+
        | skew     | skew               |
        +----------+--------------------+
        | std      | standard deviation |
        +----------+--------------------+
        | sum      | sum                |
        +----------+--------------------+
        | var      | variance           |
        +----------+--------------------+

    {groupby}
    window :
        [optional, default = 2]

        Size of the moving window. This is the number of observations used for
        calculating the statistic. Each window will be a fixed size.

        If its an offset then this will be the time period of each window. Each
        window will be a variable sized based on the observations included in
        the time-period. This is only valid for datetimelike indexes.

    min_periods : int, default None

        Minimum number of observations in window required to have a value
        (otherwise result is NA). For a window that is specified by an offset,
        this will default to 1.

    center : boolean, default False

        Set the labels at the center of the window.

    win_type : string, default None

        Provide a window type. If None, all points are evenly weighted. See the
        notes below for further information.

    on : string, optional

        For a DataFrame, column on which to calculate the rolling window,
        rather than the index

    closed : string, default None

        Make the interval closed on the 'right', 'left', 'both' or 'neither'
        endpoints. For offset-based windows, it defaults to 'right'. For fixed
        windows, defaults to 'both'. Remaining cases not implemented for fixed
        windows.

    span :
        [optional, default = 2]

        DEPRECATED: Changed to 'window' to be consistent with pandas.

    {input_ts}
    {columns}
    {start_date}
    {end_date}
    {dropna}
    {skiprows}
    {index_type}
    {names}
    {clean}
    {source_units}
    {target_units}
    {print_input}

    """
    tsd = tsutils.common_kwds(tsutils.read_iso_ts(input_ts,
                                                  skiprows=skiprows,
                                                  names=names,
                                                  index_type=index_type),
                              start_date=start_date,
                              end_date=end_date,
                              pick=columns,
                              dropna=dropna,
                              source_units=source_units,
                              target_units=target_units,
                              clean=clean,
                              groupby=groupby)

    if span is not None:
        window = span
    if window is None:
        window = 2

    window = tsutils.make_list(window)

    ntsd = pd.DataFrame()
    for win in window:
        statstr = ''
        if statistic in ['corr',
                         'count',
                         'cov',
                         'kurt',
                         'max',
                         'mean',
                         'median',
                         'min',
                         'quantile',
                         'skew',
                         'std',
                         'sum',
                         'var']:
            statstr = '.{statistic}()'.format(**locals())
        etsd = eval('''tsd.apply(lambda x:
                       x.rolling({win},
                                 min_periods={min_periods},
                                 center={center},
                                 win_type={win_type},
                                 on={on},
                                 closed={closed}){statstr}
                                 )'''.format(**locals()))
        etsd.columns = ['{0}_rolling_{1}_{2}'.format(i, win, statistic)
                        for i in etsd.columns]

        ntsd = ntsd.join(etsd, how='outer')

    return tsutils.print_input(print_input,
                               tsd,
                               ntsd,
                               None)
