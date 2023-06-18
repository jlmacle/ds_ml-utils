import os
class DataPath:

    def __init__(self) :
        self.path_to_data_folder = "Undefined"
        self.csv_name_original = "Undefined"
        self.csv_name_cleaned = "Undefined"
        self.path_to_original_data = "Undefined"
        self.path_to_cleaned_data = "Undefined"
        self.path_to_folder_with_data_for_reporting = "Undefined"
        self.file_name_for_file_with_reporting_data_in_csv_format = "Undefined"
        self.file_name_for_file_with_reporting_data_in_txt_format = "Undefined"

#  *** Getters ***

    def get_path_to_data_folder(self):
        return self.path_to_data_folder
    
    def get_file_name_for_csv_with_original_data(self):
        return self.csv_name_original
    
    def get_path_to_original_csv_file(self):
        return os.path.join(self.path_to_data_folder, self.csv_name_original)
    
    def get_file_name_for_csv_with_cleaned_data(self):          
        return self.csv_name_cleaned
    
    def get_path_to_cleaned_csv_file(self):
        return os.path.join(self.path_to_data_folder, self.csv_name_cleaned)
    
    def get_path_to_folder_with_data_for_reporting(self):
        return self.path_to_folder_with_data_for_reporting
    
    def get_file_name_for_csv_file_with_data_for_reporting(self):
        return self.file_name_for_file_with_reporting_data_in_csv_format
    
    def get_path_to_csv_file_with_data_for_reporting(self):
        return os.path.join(self.path_to_folder_with_data_for_reporting, self.file_name_for_file_with_reporting_data_in_csv_format)
    
    def get_file_name_for_txt_file_with_data_for_reporting(self):
        return self.file_name_for_file_with_reporting_data_in_txt_format
    
    def get_path_to_txt_file_with_data_for_reporting(self): 
        return os.path.join(self.path_to_folder_with_data_for_reporting, self.file_name_for_file_with_reporting_data_in_txt_format)
    

#  *** Setters ***
    def set_path_to_data_folder(self, path_to_data_folder):   
        self.path_to_data_folder = path_to_data_folder

    def set_file_name_for_csv_with_original_data(self, csv_name_original):
        self.csv_name_original = csv_name_original

    def set_file_name_for_csv_with_cleaned_data(self, csv_name_cleaned):
        self.csv_name_cleaned = csv_name_cleaned

    def set_path_to_folder_with_data_for_reporting(self, path_to_folder_with_data_for_reporting):
        self.path_to_folder_with_data_for_reporting = path_to_folder_with_data_for_reporting
    
    def set_file_name_for_csv_file_with_data_for_reporting(self, file_name_for_file_with_reporting_data_in_csv_format):
        self.file_name_for_file_with_reporting_data_in_csv_format = file_name_for_file_with_reporting_data_in_csv_format

    def set_file_name_for_txt_file_with_data_for_reporting(self, file_name_for_file_with_reporting_data_in_txt_format):
        self.file_name_for_file_with_reporting_data_in_txt_format = file_name_for_file_with_reporting_data_in_txt_format
    
    
    

    
    


