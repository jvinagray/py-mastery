1.
def fizzBuzzVariant(n):
    for num in range(1, n + 1):
        if num % 3 == 0 and num % 2 == 0:
            print("FizzBuzz", end=", ")
        elif num % 2 == 0:
            print("Fizz", end=", ")
        elif num % 3 == 0:
            print("Buzz", end=", ")
        else:
            print(num, end=", ")
    print('\n')
    

fizzBuzzVariant(30)

2.
def reverseString(string):
    char_list = list(string)
    size = len(char_list)
    reversed = [None] * size
    for i in range(len(char_list)):
        reversed[i] = char_list[-1 - i]
    reversed_word = ''.join(reversed)
    return reversed_word

print(reverseString("word"))

3.
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
evens = list[::2]
reversed_list = list[::-1]
print(evens)
print(reversed_list)

4. 
def max_of_numbers(a, b, c):
    if a > b and a > c:
        print(r"The highest of the three is {a}")
    elif b > a and b > c:
        print(r"The highest of the three is {b}")
    elif c > a and c > b:
        print(r"The highest of the three is {c}")
    elif a == b or a == c or b == c:
        print("Numbers can't be equal")

max_of_numbers(1, 2, 3)
max_of_numbers(3, 2, 1)
max_of_numbers(1, 3, 2)
max_of_numbers(1, 1, 3)
max_of_numbers(3, 3 ,1)