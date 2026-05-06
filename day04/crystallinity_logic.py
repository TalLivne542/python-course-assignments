def calculate_crystallinity(polymer_name, delta_hm_measured, moisture_content=0.0):
    """
    Calculates crystallinity % with optional moisture correction.
    Now includes an expanded polymer database.
    """
    # Expanded Database based on peer feedback (Added PVC, HDPE, LDPE, etc.)
    # Values represent Delta Hm0 (Enthalpy of 100% crystalline polymer in J/g)
    polymer_db = {
        "PE": 293.0,
        "HDPE": 293.0,
        "LDPE": 293.0,
        "PP": 207.0,
        "PET": 140.0,
        "Nylon6": 230.0,
        "PVC": 156.0,      # Added based on peer review suggestion
        "PCL": 139.5,    # Added based on peer review suggestion
        "PLA": 93.0     
    }
    
    # Normalize input to handle different casing (e.g., pvc -> PVC)
    poly_key = polymer_name.upper() if polymer_name.upper() in polymer_db else polymer_name
    
    if poly_key not in polymer_db:
        raise ValueError(f"Polymer '{polymer_name}' not found. Available: {', '.join(polymer_db.keys())}")
    
    if not (0 <= moisture_content < 100):
        raise ValueError("Moisture content must be between 0 and 99.9%.")
    
    delta_hm_zero = polymer_db[poly_key]
    
    # Enthalpy correction for moisture
    corrected_hm = delta_hm_measured / (1 - (moisture_content / 100.0))
    
    crystallinity = (corrected_hm / delta_hm_zero) * 100
    return crystallinity
