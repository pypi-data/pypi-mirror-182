# This module has more granulated functions which aid in the manipulation of data
import pandas as pd
import numpy as np

def basic_table(read_type, sheet_name, read_path, columns_to_keep, columns_rename, filters, group_by, aggregate_columns, pre_agg_math_columns, post_agg_math_columns):
    
    if read_type == 'csv':
        df_basic_table = pd.read_csv(read_path)
    elif read_type == 'excel':
        df_basic_table = pd.read_excel(read_path, sheet_name=sheet_name)
    else:
        print('read_type must be either "csv" or "excel"')
    
    df_basic_table = df_basic_table[columns_to_keep]
    df_basic_table.columns = columns_rename

    if pre_agg_math_columns != "":
        for new_column_name, math_expression in pre_agg_math_columns.items():
            df_basic_table[new_column_name] = df_basic_table.eval(math_expression)
    
    for column, operator, value in filters:
        if operator == "==":
            df_basic_table = df_basic_table[df_basic_table[column] == value]
        elif operator == "!=":
            df_basic_table = df_basic_table[df_basic_table[column] != value]
        elif operator == ">":
            df_basic_table = df_basic_table[df_basic_table[column] > value]
        elif operator == ">=":
            df_basic_table = df_basic_table[df_basic_table[column] >= value]
        elif operator == "<":
            df_basic_table = df_basic_table[df_basic_table[column] < value]
        elif operator == "<=":
            df_basic_table = df_basic_table[df_basic_table[column] <= value]

    df_basic_table = df_basic_table.groupby(group_by).aggregate(aggregate_columns).reset_index()

    if post_agg_math_columns != "":
        for new_column_name, math_expression in post_agg_math_columns.items():
            df_basic_table[new_column_name] = df_basic_table.eval(math_expression)


    return df_basic_table


