import subprocess
import pytest
import os
import sys
sys.path.append(os.path.abspath('./project'))
from data_processing.transform import (
    DeleteColumns,
    FillEmptyValues,
    FilterRows
    )
from data_processing.load import LoadDfToSqlite
import pandas as pd


PIPELINE_SCRIPT_PATH = os.path.abspath("./project/pipeline.py")
OUTPUT_FILE_PATH = os.path.abspath("./data/ChronicHealthTrends.db")

@pytest.fixture
def execute_pipeline():
    if os.path.exists(OUTPUT_FILE_PATH):
        os.remove(OUTPUT_FILE_PATH)
    
    subprocess.run(["python", PIPELINE_SCRIPT_PATH], check=True)

@pytest.fixture
def get_sample_data():
    sample_data = {
        'A': [1, 2, None, 4],
        'B': [5, None, 7, 8],
        'C': [9, 10, 11, 12]
    }
    sample_df = pd.DataFrame(sample_data)
    return sample_df

@pytest.fixture
def get_sample_config():
    config = {
        'columnsToDelete': ['B'],
        'filteringQuery': 'C > 10'
    }
    return config

def test_delete_columns(get_sample_data,get_sample_config):
    transformed_df=DeleteColumns(get_sample_data,get_sample_config['columnsToDelete'])
    assert 'B' not in transformed_df, "Column B is now deleted"


def test_filter_rows(get_sample_data,get_sample_config):
    transformed_df = FilterRows(get_sample_data,get_sample_config['filteringQuery'])
    assert len(transformed_df) == 2, "The dataframe should now contain 2 rows"


def test_fill_empty_rows(get_sample_data):
    transformed_df = FillEmptyValues(get_sample_data)
    assert not transformed_df.isnull().values.any(), "All the empty values are now removed"


def test_pipeline_output_file(execute_pipeline):
    assert os.path.exists(OUTPUT_FILE_PATH), "Output file was not created by the pipeline."


