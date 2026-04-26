# crystallinity_logic.py

# Theoretical enthalpy (J/g) for 100% crystalline polymers
POLYMER_DATA = {
    "PE": 293.0,
    "PP": 207.0,
    "PET": 140.0,
    "Nylon6": 230.0
}

def calculate_crystallinity(polymer_name, measured_hm):
    """
    Calculates the degree of crystallinity (Xc).
    Returns the percentage as a float or None if polymer not found.
    """
    if polymer_name not in POLYMER_DATA:
        return None
    
    theoretical_hm = POLYMER_DATA[polymer_name]
    xc = (measured_hm / theoretical_hm) * 100
    return xc
