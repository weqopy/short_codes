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
def fib_recursive(n):
    if n < 2:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


# 迭代
def fib_iterate(n):
    if n < 2:
        return 1
    a, b = 1, 1
    while n > 2:
        a, b = b, a + b
        n -= 1
    return b


# jupyter notebook 测试
# #递归函数在 fib_recursive(989) 时栈溢出
# 迭代函数在 fib_iterate(100000) 时为 100 ms 级别，10 ** 6 时为 10 s 级别
print(fib_recursive(10))
print(fib_iterate(10))
