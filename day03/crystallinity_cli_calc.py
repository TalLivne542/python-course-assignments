import sys

POLYMER_DATA = {"PE": 293.0, "PP": 207.0, "PET": 140.0, "Nylon6": 230.0}

if len(sys.argv) != 3:
    print("Usage: python crystallinity_cli_calc.py [Polymer_Name] [Enthalpy_Value]")
    print("Example: python crystallinity_cli_calc.py PE 150")
else:
    poly = sys.argv[1]
    try:
        hm = float(sys.argv[2])
        if poly in POLYMER_DATA:
            xc = (hm / POLYMER_DATA[poly]) * 100
            print(f"CLI Result: {poly} Crystallinity = {xc:.2f}%")
        else:
            print(f"Error: {poly} is not in the database.")
    except ValueError:
        print("Error: Enthalpy must be a number.")
