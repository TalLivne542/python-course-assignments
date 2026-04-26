from crystallinity_logic import calculate_crystallinity

def test_calculations():
    # Test 1: PE with half of its theoretical value should be 50%
    assert calculate_crystallinity("PE", 146.5) == 50.0
    
    # Test 2: PP with its full theoretical value should be 100%
    assert calculate_crystallinity("PP", 207.0) == 100.0
    
    # Test 3: Unknown polymer should return None
    assert calculate_crystallinity("Unknown", 100) is None
    
    print("All tests passed successfully!")

if __name__ == "__main__":
    test_calculations()
