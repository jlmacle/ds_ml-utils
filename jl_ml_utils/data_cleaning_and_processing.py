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
    
    def import_csv_to_df(self, path_to_csv_file, has_low_memory_option):
        return pd.read_csv(path_to_csv_file, low_memory=has_low_memory_option)

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

# 4.Duplicates removals
    def pre_pivot_table_pre_cleaning(df, column1, column2, print_data_for_unique_values):
      column1_series = df[column1]
      column1_series_unique_values = column1_series.unique()
      if print_data_for_unique_values:
            print(f"Potential values for {column1}: {column1_series_unique_values}")
      # Verification that to each value in column1_series_unique_values corresponds a unique value in column2
      # If this is not the case, looking for the least time consuming way to clean the data if possible
      for value in column1_series_unique_values:
            column1_group_data_for_specific_value = df[df[column1] == value]
            # Retrieving the column2 values from the data
            coresponding_column2_data = column1_group_data_for_specific_value[column2]
            potential_values = coresponding_column2_data.unique()
            if print_data_for_unique_values:
                  print(f"Potential values for {column2} for {column1} {value}: {potential_values}")
            if len(potential_values) > 1:
                  # List all line numbers for a given value
                  for value in potential_values:
                        line_numbers_count = sum(coresponding_column2_data == value)
                        print(f"Line numbers count for {column2} {value}: {line_numbers_count}")



# Encoding issues encountered :
 # File "C:\Python311\Lib\encodings\cp1252.py", line 23, in decode
    # return codecs.charmap_decode(input,self.errors,decoding_table)[0]
    # UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 5408: character maps to <undefined> 
    # --> Fixed by converting the file to utf-8 in reading and writing