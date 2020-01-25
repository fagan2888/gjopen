# -*- coding: utf-8 -*-
"""
Functions to download and read data.
"""

import pandas as pd

def set_datetime_index(df, keys_list):
    return df.set_index(pd.to_datetime(df[keys_list]))

def set_noaa_datetime_index(df):
    return set_datetime_index(df, ['year', 'month', 'day'])