from crystallinity_logic import calculate_crystallinity

print("--- Polymer Crystallinity (Interactive) ---")
poly = input("Enter polymer name (e.g., PE, PP): ")
try:
    hm = float(input("Enter measured Hm: "))
    result = calculate_crystallinity(poly, hm)
    if result is not None:
        print(f"Result: {result:.2f}%")
    else:
        print("Polymer not found.")
except ValueError:
    print("Invalid input.")
