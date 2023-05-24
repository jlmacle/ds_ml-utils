import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import os
import sys
from io import StringIO

# TODO : Reminder: data visualization should be accessible easily
# from the console and produced images
# Pdf generation is an additional feature that should build on this service
class DataVisualization:      

# Setting txt report related data
    def set_txt_report_file_name(self,file_name):
        self.file_name = file_name

    def set_report_folder_path(self, path_to_folder):
        self.path_to_folder = path_to_folder

# Print utilities
    # Function used to print the console output into a file
    def print_to_file(self, text: str):         
        with open(os.path.join(self.path_to_folder, self.file_name), 'w') as file:
            sys.stdout = file
            # Will print in the file
            print(text)

    # Function used to print the console output into a string
    def print_to_string(self, text):
        string = StringIO()
        sys.stdout = string
        print(text)
        sys.stdout = sys.__stdout__
        return text

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

        return self.print_to_string(sorted_table)
    
# Data stats as jpgs

    
###########################################################
# TODO: to clean up
    
    def simple_stats(self, df):
        # extra empty line for readability
        self.print_to_file(os.linesep)
        self.print_to_file("Number of rows in the df : " + str(df.shape[0]))
        self.print_to_file("Number of features : " + str(df.shape[1]))
        
        # extra empty line for readability
        self.print_to_file(os.linesep)
        self.print_to_file("Head of the df :")
        self.print_to_file(df.head())
       
        # extra empty line for readability
        self.print_to_file(os.linesep)
        self.print_to_file("Description of the df :")     
        stats = df.describe()
        self.print_to_file(stats)

    # Given a column name, get an histogram for the data in that column
    # TODO: probably space to better this code
    def histogram(self, df, column_name):
        sb.histplot(df, x=column_name)
        plt.show()

    

    