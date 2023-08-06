"""Engines for calculated zonal stats based on non-area-weighted statistics."""
import time
from abc import ABC
from abc import abstractmethod
from typing import Optional

import geopandas as gpd
import numpy as np
import pandas as pd

from gdptools.data.agg_gen_data import AggData
from gdptools.data.user_data import UserData
from gdptools.weights.calc_weight_engines import _make_valid


class ZonalEngine(ABC):
    """Base class for zonal stats engines."""

    def calc_zonal_from_aggdata(
        self, user_data: UserData, categorical: Optional[bool] = False
    ) -> pd.DataFrame:
        """calc_zonal_from_aggdata Template method for calculated zonal stats.

        _extended_summary_

        Args:
            user_data (UserData): _description_
            categorical (Optional[bool], optional): _description_. Defaults to False.

        Returns:
            pd.DataFrame: _description_
        """
        self._user_data = user_data
        self._categorical = categorical

        return self.zonal_stats()

    @abstractmethod
    def zonal_stats(self) -> pd.DataFrame:
        """Abstract method for calculating zonal stats."""
        pass


class ZonalEngineSerial(ZonalEngine):
    """Serial zonal stats engine."""

    def zonal_stats(self) -> pd.DataFrame:
        """zonal_stats Calculate zonal stats serially.

        _extended_summary_

        Returns:
            pd.DataFrame: _description_
        """
        zvars = self._user_data.get_vars()
        tstrt = time.perf_counter()
        agg_data: AggData = self._user_data.prep_agg_data(zvars[0])
        tend = time.perf_counter()
        print(f"data prepped for zonal in {tend - tstrt:0.4f} sedonds")
        ds_ss = agg_data.da

        if self._categorical:
            d_categories = list(pd.Categorical(ds_ss.values.flatten()).categories)

        tstrt = time.perf_counter()
        lon, lat = np.meshgrid(
            ds_ss[agg_data.cat_grid.X_name].values,
            ds_ss[agg_data.cat_grid.Y_name].values,
        )
        lat_flat = lat.flatten()
        lon_flat = lon.flatten()
        ds_vals = ds_ss.values.flatten()
        df_points = pd.DataFrame(
            {
                "index": np.arange(len(lat_flat)),
                "vals": ds_vals,
                "lat": lat_flat,
                "lon": lon_flat,
            }
        )
        df_points_filt = df_points[df_points.vals >= ds_ss.STATISTICS_MINIMUM]
        source_df = gpd.GeoDataFrame(
            df_points_filt,
            geometry=gpd.points_from_xy(df_points_filt.lon, df_points_filt.lat),
        )
        tend = time.perf_counter()
        print(f"converted tiff to points in {tend - tstrt:0.4f} seconds")
        source_df.set_crs(agg_data.cat_grid.proj, inplace=True)
        target_df = agg_data.feature.to_crs(agg_data.cat_grid.proj)
        target_df = _make_valid(target_df)
        target_df.reset_index()
        target_df_keys = target_df[agg_data.id_feature].values
        tstrt = time.perf_counter()
        ids_tgt, ids_src = source_df.sindex.query_bulk(
            target_df.geometry, predicate="contains"
        )
        tend = time.perf_counter()
        print(f"overlaps calculated in {tend - tstrt:0.4f} seconds")
        if self._categorical:

            val_series = pd.Categorical(
                source_df["vals"].iloc[ids_src], categories=d_categories
            )

            agg_df = pd.DataFrame(
                {
                    agg_data.id_feature: target_df[agg_data.id_feature]
                    .iloc[ids_tgt]
                    .values
                }
            )
            agg_df["vals"] = val_series
            tstrt = time.perf_counter()
            stats = agg_df.groupby(agg_data.id_feature).describe(include=["category"])
            tend = time.perf_counter()
            print(f"categorical zonal stats calculated in {tend - tstrt:0.4f} seconds")
        else:
            agg_df = pd.DataFrame(
                {
                    agg_data.id_feature: target_df[agg_data.id_feature]
                    .iloc[ids_tgt]
                    .values,
                    "vals": source_df["vals"].iloc[ids_src],
                }
            )
            tstrt = time.perf_counter()
            stats = agg_df.groupby(agg_data.id_feature).describe()
            # stats.set_index(agg_data.id_feature)
            tend = time.perf_counter()
            print(f"zonal stats calculated in {tend - tstrt:0.4f} seconds")

        tstrt = time.perf_counter()
        stats_inds = stats.index

        missing = np.setdiff1d(target_df_keys, stats_inds)
        target_df_stats = target_df.loc[
            target_df[agg_data.id_feature].isin(list(stats_inds))
        ]
        target_df_missing = target_df.loc[
            target_df[agg_data.id_feature].isin(list(missing))
        ]
        nearest = target_df_stats.sindex.nearest(
            target_df_missing.geometry, return_all=False
        )
        print(nearest)
        print(f"number of missing values: {len(missing)}")
        stats_missing = stats.iloc[nearest[1]]
        stats_tot = pd.concat([stats, stats_missing])
        stats_tot.index.name = agg_data.id_feature
        tend = time.perf_counter()
        print(
            f"fill missing values with nearest neighbors in {tend - tstrt:0.4f} seconds"
        )

        return stats_tot
