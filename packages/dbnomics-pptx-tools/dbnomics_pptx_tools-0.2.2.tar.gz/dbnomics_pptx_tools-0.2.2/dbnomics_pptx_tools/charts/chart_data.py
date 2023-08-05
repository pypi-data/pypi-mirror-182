from datetime import datetime, timedelta
from typing import Iterator, cast

import daiquiri
import numpy as np
import pandas as pd
from pandas import DataFrame, DatetimeIndex
from pptx.chart.axis import DateAxis
from pptx.chart.chart import Chart
from pptx.chart.data import CategoryChartData

from dbnomics_pptx_tools.metadata import ChartSpec
from dbnomics_pptx_tools.repo import SeriesRepo

logger = daiquiri.getLogger(__name__)


def build_category_chart_data(chart_spec: ChartSpec, *, df: DataFrame) -> CategoryChartData:
    chart_spec_series_ids = chart_spec.get_series_ids()
    chart_data = CategoryChartData()

    pivoted_df = df.pivot(index="period", columns="series_id", values="value")
    chart_data.categories = cast(DatetimeIndex, pivoted_df.index).to_pydatetime()

    for series_id in chart_spec_series_ids:
        series_spec = chart_spec.find_series_spec(series_id)
        if series_spec is None:
            raise ValueError(f"Could not find spec for series {series_id!r}")
        series_name = series_spec.name
        if series_id not in pivoted_df:
            continue
        series = pivoted_df[series_id].replace({np.NaN: None})
        chart_data.add_series(series_name, series.values)

    return chart_data


def filter_df_to_domain(df: DataFrame, *, max_datetime: datetime | None, min_datetime: datetime | None) -> DataFrame:
    if min_datetime is not None:
        df = df.query("period >= @min_datetime")
    if max_datetime is not None:
        df = df.query("period <= @max_datetime")
    return df


def from_excel_ordinal(ordinal: float, epoch: datetime | None = None) -> datetime:
    if epoch is None:
        epoch = datetime(1899, 12, 31)
    if ordinal >= 60:
        ordinal -= 1  # Excel leap year bug, 1900 is not a leap year!
    return (epoch + timedelta(days=ordinal)).replace(microsecond=0)


def get_date_axis_bounds(date_axis: DateAxis) -> tuple[datetime | None, datetime | None]:
    minimum_scale = date_axis.minimum_scale
    if minimum_scale is not None:
        minimum_scale = from_excel_ordinal(float(minimum_scale))
    maximum_scale = date_axis.maximum_scale
    if maximum_scale is not None:
        maximum_scale = from_excel_ordinal(float(maximum_scale))
    return minimum_scale, maximum_scale


def load_chart_df(chart_spec: ChartSpec, *, chart: Chart, repo: SeriesRepo) -> DataFrame:
    date_axis = chart.category_axis
    min_datetime, max_datetime = get_date_axis_bounds(date_axis)
    chart_spec_series_ids = chart_spec.get_series_ids()

    def iter_domain_dfs() -> Iterator[DataFrame]:
        for series_id in chart_spec_series_ids:
            df = repo.load(series_id)
            if df.empty:
                logger.warning("Series %r is empty", series_id)
                continue
            domain_df = filter_df_to_domain(df, min_datetime=min_datetime, max_datetime=max_datetime)
            if domain_df.empty:
                logger.warning("Series %r is not defined within the domain %r", series_id, (min_datetime, max_datetime))
                continue
            yield domain_df

    return pd.concat(iter_domain_dfs())
