# This module has more granulated functions which aid in the manipulation of data
import pandas as pd
import numpy as np

def basic_table(read_type: str, sheet_name: str, read_path: str, columns_to_keep, columns_rename):
    
    # read in the file
    if read_type == 'csv':
        df_basic_table = pd.read_csv(read_path)
    elif read_type == 'excel':
        df_basic_table = pd.read_excel(read_path, sheet_name=sheet_name)
    else:
        print('read_type must be either "csv" or "excel"')
    
    # columns to keep 
    df_basic_table = df_basic_table[columns_to_keep]

    # rename columns
    df_basic_table.columns = columns_rename

    return df_basic_table


