from errors import ConversionError

def c_to_f(c):
    return c * (9/5) + 32

def f_to_c(f):
    return (f - 32) * (5 / 9)

def lbs_to_kg(lbs):
    return lbs * 0.453592

def kg_to_lbs(kg):
    return kg * 2.20462

def ft_to_m(ft):
    return ft * .3048

def m_to_ft(m):
    return m * 3.28084

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

def convert(value, from_unit, to_unit):
    if (from_unit, to_unit) == ("c", "f"):
        return c_to_f(value)
    elif (from_unit, to_unit) == ("f", "c"):
        return f_to_c(value)
    elif (from_unit, to_unit) == ("m", "ft"):
        return m_to_ft(value)
    elif (from_unit, to_unit) == ("ft", "m"):
        return ft_to_m(value)
    elif (from_unit, to_unit) == ("lbs", "kg"):
        return lbs_to_kg(value)
    elif (from_unit, to_unit) == ("kg", "lbs"):
        return kg_to_lbs(value)
    else:
        raise ConversionError(from_unit, to_unit)

     