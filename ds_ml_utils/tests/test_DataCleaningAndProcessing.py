from ds_ml_utils.data_cleaning_and_processing import DataCleaningAndProcessing as dcp_class
from _DataPath import _DataPath as _data_path_class
import pytest

# Cleaning the data before processing
dcp = dcp_class()
_data_path = _data_path_class()
data_path = _data_path.get_data_path_object()

path_to_data = data_path.get_path_to_original_csv_file()
print("path_to_data: ", path_to_data)

# def return_df():
#     df = dcp.import_csv_to_df(path_to_data, low_memory_setting=False)
#     return df

# @pytest.fixture(name="return_df")
# def return_df_ficture():
#     return return_df()

@pytest.fixture()
def return_df():
    df = dcp.import_csv_to_df(path_to_data, low_memory_setting=False)
    return df  

# concatenate_cells_content test
def test_concatenate_cells_content(return_df):
    df = return_df
    df = dcp.concatenate_cells_content(df, separator_for_space='_')

    
    assert(False)    
    # TODO : to finish

# trim_cells_content test
def test_trim_cells_content():
    assert(False)  
    pass
    # TODO : to finish

# commas_in_cells_removal test
def test_commas_in_cells_removal():
    assert(False)  
    pass
    # TODO : to finish


# df = dcp.trim_cells_content(df)
# test_trim_cells_content(df)

# df = dcp.commas_in_cells_removal(df, separator_for_comma=' ')
# test_commas_in_cells_removal(df)



