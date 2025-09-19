import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dir_path = os.path.dirname(os.path.abspath(__file__))
data_folder = 'labo_geo_data'
data_path = os.path.join(dir_path, data_folder)
data_files = os.listdir(data_path)
data_files_csv = [f for f in data_files if f.endswith('.csv')]

def read_geophysics_data(data_file, data_path=data_path):
    """
    Reads geophysics data from a CSV file and returns a pandas DataFrame.
    
    Parameters:
    - data_file: str, name of the CSV file to read.
    - data_path: str, path to the directory containing the CSV file.
    
    Returns:
    - df: pandas DataFrame containing the geophysics data.
    """
    full_path = os.path.join(data_path, data_file)
    df = pd.read_csv(full_path)
    return df

if __name__ == "__main__":
    # Example usage
    if data_files_csv:
        df = read_geophysics_data(data_files_csv[0])
        print(df.head())
    else:
        print("No CSV files found in the data directory.")