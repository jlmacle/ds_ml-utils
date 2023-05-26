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

    # Function used to print the console output into a file
    def print_to_txt_file(self, text: str):         
        with open(os.path.join(self.path_to_folder, self.txt_file_name), 'a') as file:
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
    
    # Function used to print n lines of a file
    def print_n_lines_of_csv_file_to_csv_file(self, file_path, n):
        with open(file_path) as file:
            for i in range(n):
                self.print_to_csv_file(file.readline())

    # Function used to go from <to re-think> to CSV data
    def table_data_with_label_row_to_csv(self, data):  
        csv_string = ""              
        first_line = str(data).split("\n")[0]
        # Adding the first line to csv string
        csv_string += first_line + "\n"
        # print(first_line)
        # Removing the first line from the data
        data = str(data).replace(first_line+'\n', "")
        # print(os.linesep)
        # print(data)
        # Splitting the data into lines
        splitted_text = data.split("\n")
        for line in splitted_text:
            splitted_line = line.split()
            # print(splitted_line)
            csv_line = ""
            for item in splitted_line:
                csv_line += item + ","
            csv_line = csv_line[:-1]
            csv_string += csv_line + "\n"
            # print(csv_line)
        print(csv_string)
        return csv_string

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


    # TODO : additional print_to_csv_file / print_to_txt_file
    def simple_stats(self, df):
        # extra empty line for readability
        self.print_to_csv_file(os.linesep)
        self.print_to_csv_file("Number of rows," + str(df.shape[0]))
        self.print_to_csv_file("Number of features," + str(df.shape[1]))
        self.print_to_txt_file(os.linesep)
        self.print_to_txt_file("Number of rows\t\t" + str(df.shape[0]))
        self.print_to_txt_file("Number of features\t" + str(df.shape[1]))
        
        # extra empty line for readability
        self.print_to_txt_file(os.linesep)
        self.print_to_txt_file("Head of the cleaned data :")
        head_of_cleaned_data = df.head()
        self.print_to_txt_file(head_of_cleaned_data)        
        self.print_to_csv_file(os.linesep)
        self.print_n_lines_of_csv_file_to_csv_file(self.path_to_cleaned_data, 5)
       
        # extra empty line for readability
        self.print_to_txt_file(os.linesep)
        self.print_to_txt_file("Description of the dataframe :")     
        stats = df.describe()
        self.print_to_txt_file(stats)
        csv_stats = stats.array_with_label_row_to_csv()
        self.print_to_csv_file(csv_stats)


        self.print_to_txt_file(os.linesep)

    # Given a column name, get an histogram for the data in that column
    # TODO: probably space to better this code
    def histogram(self, df, column_name):
        sb.histplot(df, x=column_name)
        plt.show()

    

    