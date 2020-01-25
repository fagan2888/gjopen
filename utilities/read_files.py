# -*- coding: utf-8 -*-
"""
Functions to download and read data.
"""

import os
import pandas as pd
from io import StringIO
import subprocess

def download_file(url, dst, overwrite=False):
    """Download txt file by using wget command (requires wget installed on system)"""
    if os.path.exists(dst):
        if overwrite:
            os.remove(dst)
        else:
            return
    command = ["wget", url, "-o", dst]
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    output, error = process.communicate()
    print(output, error)

def read_text_file(file_path):
    """Read a txt file"""
    with open(file_path, 'r') as f:
        return f.readlines()
    
def get_first_index_without_hashtag(lines):
    for i, line in enumerate(lines):
        if not line.startswith('#'):
            return i
    return -1

def get_processed_noaa_file(lines):
    """
    the last line of comment is the column names for data
    everything below is data
    """
    i = get_first_index_without_hashtag(lines)
    assert i > 0, "Unexpected file format: please provide correct noaa.gov txt file"
    lines[i-1] = lines[i-1][1:]
    merged_text_without_comments = "".join(lines[i-1:])
    return StringIO(merged_text_without_comments)

def read_noaa_txt(file_path):
    """Read a txt file downloaded from noaa.gov into a pandas DataFrame"""
    lines = read_text_file(file_path)
    processed_str_as_file = get_processed_noaa_file(lines)
    return pd.read_csv(processed_str_as_file, delim_whitespace=True)
    

def download_and_read_noaa_txt(url, data_dir='data'):
    """Download and read a txt file from noaa.gov 
    e.g. ftp://aftp.cmdl.noaa.gov/products/trends/co2/co2_trend_gl.txt"""
    dst = os.path.join(data_dir, os.path.basename(url))
    print("Saving file as", dst)
    download_file(url, dst)
    return read_noaa_txt(dst)
