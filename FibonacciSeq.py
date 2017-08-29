def fib(n):
    assert n > 0
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


n = int(input('Input an integer number: '))
mod = input('Just want Nth digit? [y/n]: ')


def output():
    if mod == 'y':
        print(fib(n))
    elif mod == 'n':
        for i in range(1, n + 1):
            print(fib(i))


if __name__ == '__main__':
    output()
