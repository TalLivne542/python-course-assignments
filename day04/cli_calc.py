import sys
from crystallinity_logic import calculate_crystallinity

def main():
    # Expecting: python cli_calc.py [polymer] [Hm] [moisture]
    if len(sys.argv) < 3:
        print("Usage: python cli_calc.py <polymer> <Hm> [moisture]")
        return

    poly = sys.argv[1]
    hm = float(sys.argv[2])
    moist = float(sys.argv[3]) if len(sys.argv) > 3 else 0.0

    try:
        res = calculate_crystallinity(poly, hm, moist)
        print(f"Crystallinity: {res:.2f}%")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
