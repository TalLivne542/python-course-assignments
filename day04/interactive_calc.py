from crystallinity_logic import calculate_crystallinity

def run_interactive():
    print("--- Polymer Crystallinity Calculator (Moisture Correction Enabled) ---")
    try:
        poly = input("Enter polymer (PE, PP, PET, Nylon6): ").strip()
        hm = float(input("Enter measured Delta Hm (J/g): "))
        moist_in = input("Enter moisture % (default 0): ").strip()
        moist = float(moist_in) if moist_in else 0.0
        
        result = calculate_crystallinity(poly, hm, moist)
        print(f"\nResults for {poly}:")
        print(f"Crystallinity: {result:.2f}%")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_interactive()
