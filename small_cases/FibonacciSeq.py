from functools import wraps


def memo(func):
    cache = {}

    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrap


# 递归
@memo
def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# 迭代
def fib_2(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    a, b = 0, 1
    while n > 2:
        a, b = b, a + b
        n -= 1
    return b


print(fib(10))
print(fib_2(10))
