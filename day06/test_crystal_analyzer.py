import os
import pytest
from crystal_analyzer import download_and_analyze_crystal

def test_crystal_download_and_volume():
    """
    Verify that the program successfully connects to the database,
    downloads the crystal file, and computes a valid positive volume.
    """
    crystal_id = "1011110"
    expected_file = f"crystal_{crystal_id}.cif"
    
    # Clean old files if they exist
    if os.path.exists(expected_file):
        os.remove(expected_file)
        
    success, volume = download_and_analyze_crystal(crystal_id)
    
    assert success is True
    assert volume > 0, "Calculated volume should be a positive number"
    assert os.path.exists(expected_file), "The downloaded database file was not saved"

def test_invalid_crystal_id():
    """
    Verify that the program handles non-existent crystal IDs gracefully.
    """
    success, volume = download_and_analyze_crystal("0000000000")
    assert success is False
    assert volume == 0
