import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import os
import sys
from io import StringIO

class DataVisualization:      

# Setting files related data
    def set_csv_report_file_name(self,csv_file_name):
        self.csv_file_name = csv_file_name

    def set_txt_report_file_name(self, txt_file_name):
        self.txt_file_name = txt_file_name

    def set_report_folder_path(self, path_to_folder):
        self.path_to_folder = path_to_folder

    def set_path_to_cleaned_data(self, path_to_cleaned_data):
        self.path_to_cleaned_data = path_to_cleaned_data

# Print utilities
    # Functions used to print the console output into a file
    def print_to_csv_file(self, text: str):         
        with open(os.path.join(self.path_to_folder, self.csv_file_name), 'a') as file:
            sys.stdout = file
            # Will print in the file
            print(text)
            sys.stdout = sys.__stdout__

    # Function used to print the console output into a file
    def print_to_txt_file(self, text: str):         
        with open(os.path.join(self.path_to_folder, self.txt_file_name), 'a') as file:
            sys.stdout = file
            # Will print in the file
            print(text)
            sys.stdout = sys.__stdout__

    # Function used to print the output of a function with no return value into a file
    def print_function_output_and_not_the_return_value_to_txt_file(self, function, *args):
        with open(os.path.join(self.path_to_folder, self.txt_file_name), 'a') as file:
            sys.stdout = file
            # Will print in the file
            function(*args)
            sys.stdout = sys.__stdout__

    # Function used to print the output of a function with no return value into a string
    def print_function_output_and_not_the_return_value_to_string(self, function, *args):
        string = StringIO()
        sys.stdout = string
        function(*args)
        sys.stdout = sys.__stdout__
        return string.getvalue()

    # Function used to print the console output into a string
    def print_to_string(self, text):
        string = StringIO()
        sys.stdout = string
        print(text)
        sys.stdout = sys.__stdout__
        return text      
    
    # Function used to print n lines of a file
    def print_n_lines_of_csv_file_to_csv_file(self, file_path, n):
        with open(file_path) as file:
            for i in range(n):
                self.print_to_csv_file(file.readline())
    
    # Function used to print the describe info into a csv string
    def print_describe_nested_list_to_csv_string(self, nested_list):
        first_column_data = ["count", "mean", "std", "min", "25%", "50%", "75%", "max"]
        string = ""
        for i, line in enumerate(nested_list):
            string = string + first_column_data[i] + ","
            for item in line:
                string += str(item) + ","
            # Removing the last comma
            string = string[:-1]            
            string += "\n"
        return string

    # Function used to go from tabulated data to CSV data
    def table_data_to_csv(self, data, nbr_of_lines_to_ignore): 
        csv_string = ""              
        lines = str(data).split("\n")          
        elements_for_lines_to_convert_to_csv = lines[nbr_of_lines_to_ignore:]            
        
        for line in elements_for_lines_to_convert_to_csv:
            splitted_line = line.split()
            csv_line = ""
            for item in splitted_line:
                csv_line += item + ","
            csv_line = csv_line[:-1]
            csv_string += csv_line + "\n"
        return csv_string
    
    # Function used to convert to csv part of a tabulated data
    # A number of first rows is added as is in the csv file
    # The rest of the tabulated data is converted to csv
    # def tabulated_data_to_csv_with_some_rows_added_as_is(self, data, number_of_rows_to_add_as_is):
    #     csv_string = ""
    #     # Adding the first rows as is
    #     for i in range(number_of_rows_to_add_as_is):
    #         csv_string += str(data).split("\n")[i] + "\n"
    #     # Adding the rest of the data as csv
    #     csv_string += self.table_data_with_label_row_ignored_to_csv(str(data).split("\n")[number_of_rows_to_add_as_is])
    #     return csv_string

# Data stats as strings
    def get_number_of_rows(self, df):
        return str(df.shape[0])
    
    def get_number_of_features(self, df):
        return str(df.shape[1])

    # Given a column name, count the number of unique values in that column
    # and display in a sorted table 
    def count_unique_values(self, df, column_name, is_order_ascending):
        results = df[column_name].value_counts()

        sorted_table = pd.DataFrame({
            'Unique Values':results.index,
            'Count':results.values
        }).sort_values(by='Count',ascending=is_order_ascending)
       
        return sorted_table
        
    
# Data stats as jpgs
    def simple_stats(self, df):
        # extra empty line for readability
            #to txt
        self.print_to_txt_file("")
        self.print_to_txt_file("Number of rows\t" + str(df.shape[0]))
        self.print_to_txt_file("Number of features\t" + str(df.shape[1]))
            # to csv
        self.print_to_csv_file("")
        self.print_to_csv_file("Number of rows," + str(df.shape[0]))
        self.print_to_csv_file("Number of features," + str(df.shape[1]))       

        # extra empty line for readability
            # to txt
        self.print_to_txt_file("")
        self.print_to_txt_file("Dataframe info :")
        self.print_function_output_and_not_the_return_value_to_txt_file(df.info,[])
            #  to CSV
        # TODO: to finish
        # self.print_to_csv_file("")
        # self.print_to_csv_file("Dataframe info :")
        # self.print_function_output_and_not_the_return_value_to_txt_file(df.info,[])
        
        # extra empty line for readability
            #to txt
        self.print_to_txt_file("")
        self.print_to_txt_file("Head of the cleaned data :")
        head_of_cleaned_data = df.head()
        self.print_to_txt_file(head_of_cleaned_data)    
            # to csv    
        self.print_to_csv_file("")
        self.print_n_lines_of_csv_file_to_csv_file(self.path_to_cleaned_data, 5)
               
        # extra empty line for readability
            # to txt
        self.print_to_txt_file("")
        self.print_to_txt_file("Description of the dataframe :")     
        stats = df.describe()
        self.print_to_txt_file(stats)
            #  to csv
        self.print_to_csv_file("")
        self.print_to_csv_file(",Age,Fnlwgt,Education-Num,Capital gain,Capital loss,Hours-per-week")
        self.print_to_csv_file(self.print_describe_nested_list_to_csv_string(stats.values.tolist())) 

# Misc
    def get_unique_count_values_csv_row(self):
        return ",Unique Values,Count"