from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from ds_ml_utils.datas_structures.trie import Trie

import numpy as np
import pandas as pd
import re
import os

# 1. Data imports
# 2. Data encoding fixing
# 3. Row removals
# 4. Header processing
# 5. Cells processing
# 6. Column processing
# 7. Pre pivot table cleaning
# 8. Pattern finding
# 9. Information clustering

class DataCleaningAndProcessing:    
    
# 1. Data imports
    def import_csv_to_numpy_array(self, path_to_csv_file, skip_header_option):
        return np.genfromtxt(path_to_csv_file, delimiter=',' , skip_header=skip_header_option)    
    
    def import_csv_to_df(self, path_to_csv_file, low_memory_setting):
        return pd.read_csv(path_to_csv_file, low_memory=low_memory_setting)
    
    # to remember : the trie does not store duplicate values
    def import_word_list_in_file_to_list(self, path_to_file):
        list_of_words = []
        with open(path_to_file, 'r') as f:
            for line in f:
                word = line.strip()
                # an empty string evaluates to False in Python
                # TODO: to test with a list of words with empty lines
                if word:
                    list_of_words.append(word)
        return list_of_words               

# 2. Data encoding fixing 
   
    
# 3. Row removals
    def removes_rows_with_empty_data_from_column(self, df, column_name):
       df = df.dropna(subset=[column_name])
       return df     
    
    def drop_duplicates_and_remove_rows_with_only_empty_data_from_df(self, path_to_csv_folder, csv_name, low_memory_setting):
        #  low_memory parameter added to fix the following warning:
        #  DtypeWarning: Columns (76,89) have mixed types. Specify dtype option on import or set low_memory=False.
        df = pd.read_csv(os.path.join(path_to_csv_folder, csv_name), low_memory=low_memory_setting)

        df = df.drop_duplicates()
        df = df.dropna(how='all')        
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

    def trim_concatenate_lower_case_header_content(self, df, separator_to_replace_space):
        df = self.trim_header_content(df)
        df = self.concatenate_header_content(df, separator_to_replace_space)
        df.columns = df.columns.str.lower()
        return df

# 5. Cell processing  

    def trim_cells_content(self, df):
        df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
        return df
 
    def concatenate_cells_content(self, df, separator_for_space):
        print(f"-----> Converting one to many spaces to one {separator_for_space}")
        df = df.replace('[ ]+', '_', regex=True)
        return df  
    
    def remove_commas_from_df(self, df):        
        df = df.replace(',', '', regex=True)
        return df
    
    def cells_processing_basic(self, df, separator_to_replace_space):
        print("--> Cell content trimming")
        df = self.trim_cells_content(df)
        print("--> Cell content concatenation")
        df = self.concatenate_cells_content(df, separator_to_replace_space)  
        print("--> Removing commas from df")
        df = self.remove_commas_from_df(df) 

        return df

    def cells_processing_to_uppercase_in_column(self, df, column_name):
        print(f"--> Cell content to uppercase in column {column_name}")
        df[column_name] = df[column_name].str.upper()
        return df
    
    def from_dollar_strings_to_floats(self, df, column_name):
        print(f"--> Converting dollar strings to floats in {column_name} ")
        df[column_name] = df[column_name].str.replace('$', '', regex=False)
        df[column_name] = df[column_name].str.replace(',', '', regex=False)
        df[column_name] = df[column_name].astype(float)
        return df
    
    def from_several_underscore_strings_to_one(self, df):
        print("--> Converting several underscore strings to one")
        df = df.replace('[_]+', '_', regex=True)
        return df

# 6. Column processing
    def get_trie_with_words_from_column(self, df, column_name, separator):
        print(f"--> Extracting words from the cells in column {column_name} to put them in a trie")
        # Splitting the cells content into words using the '_' separator
        column_name_series = df[column_name]
        series_splitted = column_name_series.str.split(separator)
        # Creating a trie from the words
        trie = Trie()
        for list in series_splitted:
            for word in list:
                trie.insert(word)
        return trie
            

# 7. Pre pivot table cleaning
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
        # Sorting by line numbers and labels
        sorted_results = {}
        for label in results:
             for line_number in results[label]:
                 sorted_results[line_number] = label
        sorted_results = dict(sorted(sorted_results.items(), key=lambda pair: pair[0]))
        return sorted_results

# 8. Pattern finding / removal
    def locate_pattern_in_column(self, df, column_name, pattern):
        df = df[column_name]
        counter = 0
        for index, row in df.items():
            if re.search(pattern, str(row)):
                print(f"{row} in line {index+2}") 
                counter += 1
                if counter%3 == 0:
                    print()  
    
    def remove_pattern_in_column(self, df, column_name, pattern): 
        df[column_name] = df[column_name].str.replace(pattern, '', regex=True)
        return df
    
    def replace_pattern_in_column(self, df, column_name, pattern, replacement):
        df[column_name] = df[column_name].str.replace(pattern, replacement, regex=True)
        return df

# 9. Information clustering
    
  


# Encoding issues encountered :
 # File "C:\Python311\Lib\encodings\cp1252.py", line 23, in decode
    # return codecs.charmap_decode(input,self.errors,decoding_table)[0]
    # UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 5408: character maps to <undefined> 
    # --> Fixed by converting the file to utf-8 in reading and writing