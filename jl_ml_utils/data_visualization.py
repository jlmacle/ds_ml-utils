import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import os
import sys

class DataVisualization:      
    def set_txt_report_file_name(self,file_name):
        self.file_name = file_name

    def set_report_folder_path(self, path_to_folder):
        self.path_to_folder = path_to_folder
    
    def simple_stats(self, dataframe):
        # extra empty line for readability
        self.print_to_file(os.linesep)
        self.print_to_file("Number of rows in the dataframe : " + str(dataframe.shape[0]))
        self.print_to_file("Number of features : " + str(dataframe.shape[1]))
        
        # extra empty line for readability
        self.print_to_file(os.linesep)
        self.print_to_file("Head of the dataframe :")
        self.print_to_file(dataframe.head())
       
        # extra empty line for readability
        self.print_to_file(os.linesep)
        self.print_to_file("Description of the dataframe :")     
        stats = dataframe.describe()
        self.print_to_file(stats)

    # Given a column name, get an histogram for the data in that column
    # TODO: probably space to better this code
    def histogram(self, dataframe, column_name):
        sb.histplot(dataframe, x=column_name)
        plt.show()

    # Given a column name, count the number of unique values in that column
    # and display in a sorted table with label
    
    # Function overload using the default values and printing to a file
    def print_to_file(self, text_to_print: str):         
        with open(os.path.join(self.path_to_folder, self.file_name), 'w') as file:
            sys.stdout = file
            # Will print in the file
            print(text_to_print)
        
