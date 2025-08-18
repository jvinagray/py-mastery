import argparse

def c_to_f(c):
    return (c * (9/5)) + 32

def f_to_c(f):
    return (f - 32) * (5/9)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert temperatures between Celsius and Fahrenheit")
    parser.add_argument("value", type=float, help="Temperature value to convert")
    parser.add_argument("--to", choices=["C", "F"], required=True, help="Unit to convert to")
    args = parser.parse_args()

    if args.to == "F":
        print(f"{args.value}C = {c_to_f(args.value):.2f}F")
    else:
        print(f"{args.value}F = {f_to_c(args.value):.2f}C")