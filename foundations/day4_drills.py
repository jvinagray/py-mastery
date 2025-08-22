import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from scratch.math_utils import add, subtract, multiply, divide, remainder
from scratch.tools import is_prime, reverse_string

print(add(1, 5))
print(subtract(5, 2))
print(multiply(5, 8))
print(divide(50, 15))
print(remainder(100, 8))
print(is_prime(3791))
print(reverse_string("armageddon"))
