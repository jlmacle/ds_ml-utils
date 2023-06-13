from ds_ml_utils.data_cleaning_and_processing import DataCleaningAndProcessing as dcp_class
from _DataPath import _DataPath as _data_path_class
import pytest, string, os

# Cleaning the data before processing
dcp = dcp_class()
_data_path = _data_path_class()
data_path = _data_path.get_data_path_object()

path_to_original_data = data_path.get_path_to_original_csv_file()
path_to_data_after_trimming = os.path.join(data_path.get_path_to_data_folder(), 'test_trim_cells_content.csv')
path_to_data_after_concatenation = os.path.join(data_path.get_path_to_data_folder(), 'test_concatenate_cells_content.csv')
path_to_data_after_commas_removal = os.path.join(data_path.get_path_to_data_folder(), 'test_commas_in_cells_removal.csv')
df = None

def letter_to_number(column_letter):
    letter = column_letter.upper()
    alphabet_upper = string.ascii_uppercase
    index = alphabet_upper.index(letter)
    return index

def get_cell_content(df, column_letter, row_number):
    #Converting column letter to column number
    # The letter index already starts at 0
    # -1 on the row number to ignore the header row
    column_number = letter_to_number(column_letter)
    cell_content = df.iloc[(row_number-1, column_number)]
    return cell_content

@pytest.fixture()
def return_df_original_data():
    df = dcp.import_csv_to_df(path_to_original_data, low_memory_setting=False)
    return df  

@pytest.fixture()
def return_df_after_trimming():
    df = dcp.import_csv_to_df(path_to_data_after_trimming, low_memory_setting=False)
    return df  

@pytest.fixture()
def return_df_after_concatenation():
    df = dcp.import_csv_to_df(path_to_data_after_concatenation, low_memory_setting=False)
    return df

# trim_cells_content test
# trimming before the concatenation to avoid beggining and ending separators
@pytest.mark.dependency()
def test_trim_cells_content(return_df_original_data):
    df = return_df_original_data
    df = dcp.trim_cells_content(df)
    df.to_csv(path_to_data_after_trimming, index=False)

    # Testing that the trimming occured if cell is G6
    # The header seems to be skipped when using iloc
    data_if_trimmed = "G6-Handlers-cleaners"
    produced_data = get_cell_content(df, 'G', 5)
    assert(produced_data == data_if_trimmed)  

# concatenate_cells_content test
@pytest.mark.dependency(depends=['test_trim_cells_content'])
def test_concatenate_cells_content(return_df_after_trimming):
    df = return_df_after_trimming
    df = dcp.concatenate_cells_content(df, separator_for_space='_') 
    df.to_csv(path_to_data_after_concatenation, index=False)
    # *** Staying away from header data when using iloc ***
    # Testing that the concatenation occured if cell is F2
    data_if_concatenated = "15_F2_CCC_Never_married"
    produced_data = get_cell_content(df, 'F', 1)
    assert( (data_if_concatenated   == produced_data ) )

# commas_in_cells_removal test
@pytest.mark.dependency(depends=['test_concatenate_cells_content'])
def test_commas_in_cells_removal(return_df_after_concatenation):
    df = return_df_after_concatenation
    df = dcp.commas_in_cells_removal(df,"")
    df.to_csv(path_to_data_after_commas_removal, index=False)
    # Testing that the commas are removed if cell is E6
    data_if_commas_removed = "E6-9"
    produced_data = get_cell_content(df, 'E', 5)
    assert( (data_if_commas_removed   == produced_data ) )
    




