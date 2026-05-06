def calculate_crystallinity(polymer_name, delta_hm_measured, moisture_content=0.0):
    """
    Calculates the crystallinity percentage, with an optional moisture correction.
    Formula: Corrected_Hm = Measured_Hm / (1 - Moisture%/100)
    """
    polymer_db = {
        "PE": 293.0,
        "PP": 207.0,
        "PET": 140.0,
        "Nylon6": 230.0
    }
    
    if polymer_name not in polymer_db:
        raise ValueError(f"Polymer '{polymer_name}' not found in database.")
    
    # Validation for moisture
    if not (0 <= moisture_content < 100):
        raise ValueError("Moisture content must be between 0 and 99.9%.")
    
    delta_hm_zero = polymer_db[polymer_name]
    
    # Applying moisture correction to the measured enthalpy
    corrected_hm = delta_hm_measured / (1 - (moisture_content / 100.0))
    
    crystallinity = (corrected_hm / delta_hm_zero) * 100
    return crystallinity
