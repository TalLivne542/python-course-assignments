import os
import pandas as pd
import pytest
from dsc_plotter import generate_dsc_plot

# Test file name
TEST_FILE = '10-ec-165c-annealing-18h-air.csv'

def test_output_file_generation():
    """
    Requirement: Verify that the program creates the output plot file.
    """
    # Remove plot if it exists from previous runs
    if os.path.exists("dsc_analysis_output.png"):
        os.remove("dsc_analysis_output.png")
    
    # Run the plotter
    success = generate_dsc_plot(TEST_FILE)
    
    # Verification
    assert success is True
    assert os.path.exists("dsc_analysis_output.png"), "The output graph file was not created."

def test_data_integrity():
    """
    Requirement: Verify that the script correctly skips 3 rows and reads numeric data.
    """
    # We read the file manually in the test to compare with the script's logic
    # Skipping 3 rows: Title, Column Names, Units
    df = pd.read_csv(TEST_FILE, skiprows=3, names=['Temperature', 'Heat Flow (Normalized)'])
    
    # Verify that we have numeric data and not strings from headers/units
    assert pd.api.types.is_numeric_dtype(df['Temperature']), "Temperature column contains non-numeric data (Check skip-rows logic)"
    assert pd.api.types.is_numeric_dtype(df['Heat Flow (Normalized)']), "Heat Flow column contains non-numeric data"
    assert len(df) > 0, "The data frame is empty"

def test_file_not_found():
    """
    Verify that the program handles missing files gracefully.
    """
    success = generate_dsc_plot('non_existent_file.csv')
    assert success is False

if __name__ == "__main__":
    # This allows running the tests directly with 'python test_dsc_analysis.py'
    pytest.main([__file__])
