def memoize(func):
    cache = {} # dictionary to store results

    def wrapper(arg):
        if arg in cache:
            return cache[arg]
        result = func(arg)
        cache[arg] = result
        return result

    return wrapper

import time

start_time = time.time()
@memoize
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(40))

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Executed in {elapsed_time:.6f} seconds")