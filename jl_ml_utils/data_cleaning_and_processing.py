import numpy as np
import pandas as pd
import os

class DataCleaningAndProcessing:
    def import_csv_to_numpy_array(self, path_to_csv_file):
        return np.genfromtxt(path_to_csv_file, delimiter=',',skip_header=0)
    
    def import_csv_to_dataframe(self, path_to_csv_file):
        return pd.read_csv(path_to_csv_file)

    def data_cleaning(self, path_to_csv_folder, csv_name):
        self.remove_rows_with_data_unavailable_from_csv_file(path_to_csv_folder, csv_name)
    
    def remove_rows_with_data_unavailable_from_csv_file(self, path_to_csv_folder, csv_name):
        data_frame = pd.read_csv(os.path.join(path_to_csv_folder, csv_name))
        data_frame = data_frame.dropna()
        # Creation of cleaned file name from original csv file name
        cleaned_csv_name = csv_name.split('.')[0] + "_na_removed.csv"
        data_frame.to_csv(os.path.join(path_to_csv_folder,cleaned_csv_name),index=False)
        

