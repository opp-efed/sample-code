import os
import numpy as np
import pandas as pd


def combine_tables(table_dir):
    """ Combine tables with similar headings """
    full_table = None
    for f in os.listdir(table_dir):
        table_path = os.path.join(table_dir, f)
        table = pd.read_csv(table_path)
        if full_table is None:
            full_table = table
        else:
            full_table = pd.concat([full_table, table])
    return full_table


def load_table(in_path):
    """ Load a compressed numpy array as a pandas dataframe """
    return pd.DataFrame(**np.load(in_path))


def save_table(table, out_path):
    """ Save a pandas dataframe as a compressed numpy array """
    np.savez_compressed(out_path, data=table.as_matrix(), columns=table.columns)


def main():
    table_dir = 'sample_tables'
    compressed_file = 'combined_tables.npz'

    # Read all tables and combine
    combined_table = combine_tables(table_dir)

    # Save combined tables to compressed file
    save_table(combined_table, compressed_file)

    del combined_table

    # Load table from file and select rows
    combined_table = load_table(compressed_file)

    print(combined_table)

    rows_of_interest = combined_table[combined_table.Value > 2]

    print(rows_of_interest)

main()
