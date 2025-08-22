from conversions import *
from errors import ConversionError
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Temperatures, Weight and Length between standard units")
    parser.add_argument("value", type=float, help="Value to convert")
    parser.add_argument("--from", dest="from_unit", required=True, help="Unit being converted from")
    parser.add_argument("--to", dest="to_unit", required=True, help="Unit being converted to")
    args = parser.parse_args()

    from_unit = normalize_units(args.from_unit)
    to_unit = normalize_units(args.to_unit)

    if from_unit is None or to_unit is None:
        print("Invalid unit specified!")
        exit(1)
    try:
        result = convert(args.value, from_unit, to_unit)
        print(f"{args.value} {from_unit} = {result:.2f} {to_unit}")
    except ConversionError as e:
        print(f"Not a valid conversion. Units not compatible: {e}")

    