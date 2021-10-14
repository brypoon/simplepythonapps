import time

# 5! = 120:
#
# 5 * 4 * 3 * 2 * 1

def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)

# print(f"5!={factorial(5):,}, 3!={factorial(3):,}, 11!={factorial(11):,}")



# Fibonacci numbers:
# 1, 1, 2, 3, 5, 8, 13, 21, ...

def fibonacci(limit):
    nums = []

    current = 0
    next = 1

    while current < limit:
        current, next = next, next + current
        nums.append(current)
    
    return nums

print("via lists")
start = time.process_time()
for n in fibonacci(100000):
    print(n, end=', ')
print(time.process_time() - start)


def fibonacci_co():
    current = 0
    next = 1

    while True:
        current, next = next, next + current
        yield current

print("via yield")
start = time.process_time()
for n in fibonacci_co():
    if n > 100000:
        break
    print(n, end=', ')
print(time.process_time() - start)