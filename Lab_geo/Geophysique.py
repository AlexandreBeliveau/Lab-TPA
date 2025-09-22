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

def filter_signal(signal, window_size=5):
    # Convert to numeric and apply rolling mean with window size 5
    numeric_signal = pd.to_numeric(signal, errors='coerce')
    filtered_signal = numeric_signal.rolling(window=window_size, min_periods=1, center=True).mean()
    return filtered_signal.to_numpy()

def zero_correction(signal, x, threshold=0):
    indices = np.where(x < threshold)[0]
    zero_value = np.nanmean(signal[indices])
    return signal - zero_value



if __name__ == "__main__":
    # Example usage
    if data_files_csv:
        temps = []
        distance = []
        for index in range(len(data_files_csv)):
            file_name = data_files_csv[index]
            if not file_name.endswith('3.csv'):
                continue
            df = read_geophysics_data(file_name)
            
            x = pd.to_numeric(df.iloc[:, 0], errors='coerce').to_numpy()
            
            for i in range(1, 5):
                y = filter_signal(df.iloc[:, i], window_size=20)
                y = abs(y)
                # temps.append(x[np.nanargmax(y)])
                centroid = np.nansum(x * y) / np.nansum(y)
                temps.append(centroid)

                ini_distance = float(file_name.split('m')[0].replace('_', '.'))
                distance.append(ini_distance + (4-i) * 0.25)

                # plt.plot(x, y)
                plt.title(f'{ini_distance + (4-i) * 0.25}')
                plt.legend()
                # plt.show()
    else:
        print("No CSV files found in the data directory.")




#expérience 3
import matplotlib.pyplot as plt

# Distances (in meters) and corresponding times (in seconds)
distances = [
    0.25, 0.375, 0.5, 0.625, 0.75, 0.875, 1.0, 1.125, 1.25, 1.5, 1.75, 2.0
]
times = [
    0.00151, 0.002316, 0.00234, 0.003255, 0.003964, 0.0049, 0.004515, 0.00523, 0.0031, 0.0033, 0.0037, 0.0042
]

plt.figure(figsize=(8, 5))
plt.plot(distances, times, 'o-', label='Expérience 3')
plt.xlabel('Distance (m)')
plt.ylabel('Temps (s)')
plt.title('Expérience 3: Temps en fonction de la distance')
plt.grid(True)
plt.legend()
plt.show()