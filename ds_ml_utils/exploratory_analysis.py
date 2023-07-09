import numpy as np
import pandas as pd

class ExploratoryAnalysis:  

    def is_nan(self, x):
        return (x is np.nan or x != x)

    def has_mixed_data_types(self, list):
        data_types = set(type(element) for element in list)
        return len(data_types) > 1

    def list_vertically_with_separator_to_string(self, list, string_delimiter):
        # Printing the column names, in alphabetical order,
        # one by line
        for i in range(len(list)):
            if self.is_nan(list[i]):
                list[i] = "NaN" # List cannot be sorted if it contains NaN
        # Sorting the list if there is no mixed data types
        if not self.has_mixed_data_types(list):
            list = sorted(list)
        list = [string_delimiter+str(list_item)+string_delimiter + '\n' for list_item in list]
        list = ''.join(list)
        return list
    
    def print_unique_values_to_file(self, df, file_name):
        # Printing the unique values for each column
        # to a file
        with open(file_name, 'w') as f:                    
            column_names  = df.columns
            for column_name in column_names:
                unique_values = df[column_name].unique() # df[column_name].unique() is of type numpy.ndarray
                f.write(column_name + '\n')
                if df[column_name].dtype == 'object':
                    unique_values = self.list_vertically_with_separator_to_string(unique_values.tolist(), "*")  
                else:
                    # Sorting the unique values
                    unique_values = sorted(unique_values)   
                f.write(str(unique_values) + '\n')
                f.write('\n')