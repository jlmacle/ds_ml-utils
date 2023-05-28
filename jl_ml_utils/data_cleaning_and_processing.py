import numpy as np
import pandas as pd
import chardet
import os

class DataCleaningAndProcessing:    

    def import_csv_to_numpy_array(self, path_to_csv_file):
        return np.genfromtxt(path_to_csv_file, delimiter=',',skip_header=0)
    
    def import_csv_to_df(self, path_to_csv_file):
        return pd.read_csv(path_to_csv_file)

    # def data_cleaning(self, path_to_csv_folder, csv_name):
    #     self.remove_rows_with_data_unavailable_from_csv_file(path_to_csv_folder, csv_name)
    
    def remove_rows_with_data_unavailable_from_csv_file(self, path_to_csv_folder, csv_name):
        data_frame = pd.read_csv(os.path.join(path_to_csv_folder, csv_name))
        data_frame = data_frame.dropna()
        # Creation of cleaned file name from original csv file name
        cleaned_csv_name = csv_name.split('.')[0] + "_na_removed.csv"
        data_frame.to_csv(os.path.join(path_to_csv_folder,cleaned_csv_name),index=False)

    def remove_rows_with_commas_only(self, path_to_csv_folder, csv_name, cleaned_csv_name, number_of_commas_in_empty_row):
        with open(os.path.join(path_to_csv_folder, csv_name), 'r') as file:
            with open(os.path.join(path_to_csv_folder, cleaned_csv_name), 'w') as output_file:
                for line in file:
                    if (number_of_commas_in_empty_row*',') not in line:
                        output_file.write(line)

    def convert_csv_to_utf8(self, path_to_csv_folder, cleaned_csv_name):
        with open(os.path.join(path_to_csv_folder, cleaned_csv_name), 'r') as file:
            line_nbr = 0
            with open(os.path.join(path_to_csv_folder, cleaned_csv_name.split('.')[0] + "_utf8.csv"), 'w', encoding="utf-8") as output_file:
                for line in file:
                    line_nbr += 1
                    print(f"{line_nbr} : {line}")
                    output_file.write(line)

    # Checking the data ending and fixing potential issues
    def check_and_fix_data_encoding(self, path_to_file_folder, file_name):
        with open(os.path.join(path_to_file_folder, file_name), 'rb') as file:
            data = file.read()
            result = chardet.detect(data)
            encoding = result['encoding']
            decoded_data = data.decode(encoding)

            path_to_output_file = os.path.join(path_to_file_folder, file_name.split('.')[0] + "_1_encoding_fixed.csv")
            with open(path_to_output_file, 'w', encoding=encoding) as file:
                file.write(decoded_data)

    

    