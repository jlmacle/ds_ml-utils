import numpy as np
import pandas as pd
import os

# 1. Data imports
# 2. Data encoding fixing
# 3. Row removals

class DataCleaningAndProcessing:    
# 1. Data imports
    def import_csv_to_numpy_array(self, path_to_csv_file, skip_header_option):
        return np.genfromtxt(path_to_csv_file, delimiter=',' , skip_header=skip_header_option)
    
    
    def import_csv_to_df(self, path_to_csv_file, hasLowMemoryOption):
        return pd.read_csv(path_to_csv_file, low_memory=hasLowMemoryOption)

# 2. Data encoding fixing 
   
    
# 3. Row removals

    def remove_rows_with_data_unavailable_from_csv_file(self, path_to_csv_folder, csv_name):
        data_frame = pd.read_csv(os.path.join(path_to_csv_folder, csv_name))
        data_frame = data_frame.dropna()
        # Creation of cleaned file name from original csv file name
        cleaned_csv_name = csv_name.split('.')[0] + "_na_removed.csv"
        data_frame.to_csv(os.path.join(path_to_csv_folder,cleaned_csv_name),index=False)

    def remove_rows_with_commas_only(self, path_to_csv_folder, csv_name, number_of_commas_in_empty_row):
        with open(os.path.join(path_to_csv_folder, csv_name), 'r', encoding='utf-8') as file:
            cleaned_csv_name = csv_name.split('.')[0] + "_1_rows-with-commas-only-removed.csv"
            with open(os.path.join(path_to_csv_folder, cleaned_csv_name), 'w', encoding='utf-8') as output_file:
                for line in file:
                    if (number_of_commas_in_empty_row*',') not in line:
                        output_file.write(line)


# Encoding issues encountered :
 # File "C:\Python311\Lib\encodings\cp1252.py", line 23, in decode
    # return codecs.charmap_decode(input,self.errors,decoding_table)[0]
    # UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 5408: character maps to <undefined> 
    # --> Fixed by converting the file to utf-8 in reading and writing