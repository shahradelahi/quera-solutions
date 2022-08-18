def f(x):
    if x == 0:
        return 5
    if x % 2 == 0:
        return f(x - 1) - 21
    return f(x - 1) * f(x - 1)


print(f(int(input())))
