import numpy as np
import pandas as pd
import os

# 1. Data imports
# 2. Data encoding fixing
# 3. Row removals
# 4. Header processing
# 5. Cells processing
# 6. Pre pivot table cleaning

class DataCleaningAndProcessing:    
# 1. Data imports
    def import_csv_to_numpy_array(self, path_to_csv_file, skip_header_option):
        return np.genfromtxt(path_to_csv_file, delimiter=',' , skip_header=skip_header_option)    
    
    def import_csv_to_df(self, path_to_csv_file, low_memory_setting):
        return pd.read_csv(path_to_csv_file, low_memory=low_memory_setting)

# 2. Data encoding fixing 
   
    
# 3. Row removals
    def drop_duplicates_and_remove_rows_with_data_unavailable_from_csv_file(self, path_to_csv_folder, csv_name, low_memory_setting):
        #  low_memory parameter added to fix the following warning:
        #  DtypeWarning: Columns (76,89) have mixed types. Specify dtype option on import or set low_memory=False.
        df = pd.read_csv(os.path.join(path_to_csv_folder, csv_name), low_memory=low_memory_setting)

        df = df.drop_duplicates()
        df = df.dropna()        
        return df

    def remove_rows_with_commas_only(self, path_to_csv_folder, csv_name, number_of_commas_in_empty_row, low_memory_setting):
        with open(os.path.join(path_to_csv_folder, csv_name), 'r', encoding='utf-8') as file:
            cleaned_csv_name = csv_name.split('.')[0] + "-rows_with_commas_only_removed.csv"
            with open(os.path.join(path_to_csv_folder, cleaned_csv_name), 'w', encoding='utf-8') as output_file:
                for line in file:
                    if (number_of_commas_in_empty_row*',') not in line:
                        output_file.write(line)
        df = pd.read_csv(os.path.join(path_to_csv_folder, cleaned_csv_name), low_memory=low_memory_setting)
        return df

# 4. Header processing
    def trim_header_content(self, df):
        print("--> Header content trimming")
        df.columns = df.columns.str.strip()
        return df

    def concatenate_header_content(self,df,separator_for_space):
        print("--> Header content concatenation ")
        df.columns = df.columns.str.replace(' ', separator_for_space)
        return df   

    def header_processing(self, df, separator_to_replace_space):
        df = self.trim_header_content(df)
        df = self.concatenate_header_content(df, separator_to_replace_space)
        return df

# 5. Cell processing  

    def trim_cells_content(self, df):
        df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
        return df
 
    def concatenate_cells_content(self, df, separator_for_space):
        df = df.apply(lambda x: x.str.replace(" ",separator_for_space) if x.dtype == "object" else x)
        return df    
    
    def cells_processing(self, df, separator_to_replace_space):
        print("--> Cell content trimming")
        df = self.trim_cells_content(df)
        print("--> Cell content concatenation")
        df = self.concatenate_cells_content(df, separator_to_replace_space)
        
        return df
    
# 6. Pre pivot table cleaning
    def pre_pivot_table_cleaning_need_detection(self, df, column1, column2, print_data_for_unique_values):
      results_dict = {}
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
                        # Adding to a list the line numbers for a given value
                        results_dict[value] = line_numbers_count
            # Sorting the dictionary to list the values with the least occurrences first
            
      results_dict = dict(sorted(results_dict.items(), key=lambda item: item[1], reverse=False))
      return results_dict
    
    def line_finding_given_labels_and_column(self, df, column, labels_list):
        results = {}
        for label in labels_list:            
                mask = df[column] == label               
                df_for_lines = df[mask]
                line_numbers = df_for_lines.index.tolist()  
                # numbers need to be incremented by 1
                # because the first line is the header 
                line_numbers_updated = [x + 1 for x in line_numbers]
                results[label] = line_numbers_updated
        print(f"Lines numbers where {labels_list} can be found :")
        print(results)
        return results


# Encoding issues encountered :
 # File "C:\Python311\Lib\encodings\cp1252.py", line 23, in decode
    # return codecs.charmap_decode(input,self.errors,decoding_table)[0]
    # UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 5408: character maps to <undefined> 
    # --> Fixed by converting the file to utf-8 in reading and writing