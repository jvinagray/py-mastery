from conversions import *
import argparse

units = {
    "c": ["c", "cel", "celsius"],
    "f": ["f", "fahrenheit"],
    "m": ["m", "meter", "meters"],
    "ft": ["ft", "feet"],
    "lbs": ["lbs", "pounds"],
    "kg": ["kg", "kilograms", "kilo"],
}

convertible_units = [("c", "f"), ("f", "c"), ("ft", "m"), ("m", "ft"), ("kg", "lbs"), ("lbs", "kg")]

def normalize_units(input_unit):
    input_unit = input_unit.lower()
    for key, aliases in units.items():
        if input_unit in aliases:
            return key
    return None

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

    if (from_unit, to_unit) == ("c", "f"):
        result = c_to_f(args.value)
    elif (from_unit, to_unit) == ("f", "c"):
        result = f_to_c(args.value)
    elif (from_unit, to_unit) == ("m", "ft"):
        result = m_to_ft(args.value)
    elif (from_unit, to_unit) == ("ft", "m"):
        result = ft_to_m(args.value)
    elif (from_unit, to_unit) == ("lbs", "kg"):
        result = lbs_to_kg(args.value)
    elif (from_unit, to_unit) == ("kg", "lbs"):
        result = kg_to_lbs(args.value)
    else:
        result = "That's not a built in conversion. Please try again!"

    print(result)