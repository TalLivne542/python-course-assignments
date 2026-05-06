import pytest
from crystallinity_logic import calculate_crystallinity

def test_basic_calculation():
    # PE: 146.5 J/g / 293 J/g = 50%
    assert round(calculate_crystallinity("PE", 146.5, 0), 1) == 50.0

def test_moisture_impact():
    # With 20% moisture, the measured Hm should be corrected upwards
    # If measured Hm is 80 and moisture is 20%, corrected Hm is 100.
    # For PET (Delta Hm0 = 140), result should be (100/140)*100 = 71.43
    res = calculate_crystallinity("PET", 80, 20)
    assert round(res, 2) == 71.43

def test_moisture_error():
    with pytest.raises(ValueError):
        calculate_crystallinity("PE", 100, 100) # Cannot be 100% moisture
