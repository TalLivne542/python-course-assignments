# Theoretical enthalpy (J/g)
POLYMER_DATA = {"PE": 293.0, "PP": 207.0, "PET": 140.0, "Nylon6": 230.0}

print("--- Polymer Crystallinity Calculator (Interactive Mode) ---")
poly = input("Enter polymer type (PE, PP, PET, Nylon6): ")

if poly in POLYMER_DATA:
    try:
        hm = float(input(f"Enter measured Delta Hm (J/g) for {poly}: "))
        xc = (hm / POLYMER_DATA[poly]) * 100
        print(f"Result: The degree of crystallinity for {poly} is {xc:.2f}%")
    except ValueError:
        print("Error: Please enter a valid number for enthalpy.")
else:
    print("Error: Polymer not found in database.")
