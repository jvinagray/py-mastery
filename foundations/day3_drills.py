#1.
def my_partial(func, *fixed_args, **fixed_kwargs):
    def wrapper(*args, **kwargs):
        return func(*fixed_args, *args, *fixed_kwargs, **kwargs)
    return wrapper

def multiply(a, b): return a * b

double = my_partial(multiply, 2)

print(double(10))

#2.
import math

def compose(f, g):
    def wrapper(x):
        return f(g(x))
    return wrapper

def diameter(r):
    return 2 * r

def sqr_inscribe(d):
    s = round(d / math.sqrt(2), 2)
    area = round(s * s, 2)
    return f"The side length of a sqaure inscribed in a circle of diameter {d} is {s} long and the area is {area}."

h = compose(sqr_inscribe, diameter)
print(h(241))
