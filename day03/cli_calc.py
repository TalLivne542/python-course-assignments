import sys
from crystallinity_logic import calculate_crystallinity

if len(sys.argv) == 3:
    poly = sys.argv[1]
    try:
        hm = float(sys.argv[2])
        result = calculate_crystallinity(poly, hm)
        if result is not None:
            print(f"CLI Result: {result:.2f}%")
        else:
            print("Polymer not found.")
    except ValueError:
        print("Enthalpy must be a number.")
else:
    print("Usage: python cli_calc.py [Polymer] [Value]")
