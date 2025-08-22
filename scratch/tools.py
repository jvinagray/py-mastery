def reverse_string(string):
    chars = list(string)
    reversed_list = chars[::-1]
    reversed = ''.join(reversed_list)
    return reversed

from math import floor

def is_prime(n):
    if n <= 1:
        return False
    elif n % 2 == 0:
        return False
    else:
        sqrt = n ** (1/2)
        for x in range(3, floor(sqrt), 2):
            if n % x == 0:
                return False
            else:
                return True

print(is_prime(3791))