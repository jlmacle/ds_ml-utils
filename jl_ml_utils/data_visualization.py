import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import os

class DataVisualization:
    def simple_stats(self, dataframe):

        # extra empty line for readability
        print(os.linesep)
        print("Number of rows in the dataframe : ", dataframe.shape[0])
        print("Number of features : ", dataframe.shape[1])

        # extra empty line for readability
        print(os.linesep)
        print("Head of the dataframe :")
        print(dataframe.head())

        # extra empty line for readability
        print(os.linesep) 
        print("Description of the dataframe :")       
        stats = dataframe.describe()
        print(stats)

    # Given a column name, get an histogram for the data in that column
    # TODO: probably space to better this code
    def histogram(self, dataframe, column_name):
        sb.histplot(dataframe, x=column_name)
        plt.show()

    # Given a column name, count the number of unique values in that column
    # and display in a sorted table with label

       