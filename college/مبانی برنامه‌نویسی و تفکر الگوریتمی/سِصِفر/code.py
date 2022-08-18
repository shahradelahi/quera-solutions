def f(x):
    if x == 0:
        return 1
    if x == 1:
        return 2
    if x == 2:
        return 4
    return f(x - 1) + f(x - 2) + f(x - 3)


n = int(input())
print(f(n))
