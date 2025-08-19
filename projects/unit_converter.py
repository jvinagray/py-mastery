import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert temperatures between Celsius and Fahrenheit")
    parser.add_argument("value", type=float, help="Temperature value to convert")
    parser.add_argument("--from", dest="from_unit", choices=["C", "F", "M", "FT"], required=True, help="Unit being converted from")
    parser.add_argument("--to", dest="to_unit", choices=["C", "F", "M", "FT"], required=True, help="Unit to convert to")
    args = parser.parse_args()

    conversions = {
        ("C", "F"): lambda c: (c * (9/5)) + 32,
        ("F", "C"): lambda f: (f - 32) * (5/9),
        ("M", "FT"): lambda m: m * 3.28084,
        ("FT", "M"): lambda ft: ft / 3.28084
    }

    from_unit = args.from_unit
    to_unit = args.to_unit

    if (from_unit, to_unit) in conversions:
        result = conversions[(from_unit, to_unit)](args.value)
        print(f"{args.value}{from_unit} = {result:.2f} {to_unit}")
    else:
        print(f"Conversion from {from_unit} to {to_unit} not available.")