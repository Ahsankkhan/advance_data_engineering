import subprocess
import pytest
import os


PIPELINE_SCRIPT_PATH = os.path.abspath("./project/pipeline.py")
OUTPUT_FILE_PATH = os.path.abspath("./data/ChronicHealthTrends.db")

@pytest.fixture
def execute_pipeline():
    if os.path.exists(OUTPUT_FILE_PATH):
        os.remove(OUTPUT_FILE_PATH)
    
    subprocess.run(["python", PIPELINE_SCRIPT_PATH], check=True)

def test_pipeline_output_file(execute_pipeline):


    assert os.path.exists(OUTPUT_FILE_PATH), "Output file was not created by the pipeline."
