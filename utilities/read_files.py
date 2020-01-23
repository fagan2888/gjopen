# -*- coding: utf-8 -*-
"""
Callbacks implementation. Inspired by Keras.
"""

import os
import pandas as pd
from io import StringIO
import subprocess

def download_file(url, dst, overwrite=False):
    if os.path.exists(dst):
        if overwrite:
            os.remove(dst)
        else:
            return
    command = ["wget", url, "-o", dst]
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    output, error = process.communicate()
    print(output, error)
#     wget.download(url, dst)
#     r = requests.get(url)

#     with open(dst, 'wb') as f:
#         f.write(r.content)

#     # Retrieve HTTP meta-data
#     print(r.status_code)
#     print(r.headers['content-type'])
#     print(r.encoding)

def read_text_file(file_path):
    """Read a txt file """
    with open(file_path, 'r') as f:
        return f.readlines()
    
def get_first_index_without_hashtag(lines):
    for i, line in enumerate(lines):
        if not line.startswith('#'):
            return i
    return -1

def get_processed_noaa_file(lines):
    """TODO: Does the lines already contain newline character?"""
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
    

def download_and_read_noaa_txt(url, data_dir='.'):
    """Download and read a txt file from noaa.gov 
    e.g. ftp://aftp.cmdl.noaa.gov/products/trends/co2/co2_trend_gl.txt"""
    dst = os.path.join(data_dir, os.path.basename(url))
    print("Saving file as", dst)
    download_file(url, dst)
    return read_noaa_txt(dst)