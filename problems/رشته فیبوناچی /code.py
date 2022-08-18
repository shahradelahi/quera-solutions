def fib(n, arr):
    if n == 1:
        if arr[n] == 0:
            arr[n] = 1
        return arr[n]
    if n == 2:
        if arr[n] == 0:
            arr[n] = 2
        return arr[n]
    if arr[n] == 0:
        arr[n] = fib(n - 1, arr) + fib(n - 2, arr)
    return arr[n]


t = []
for x in range(1, 100):
    array = [0 for i in range(x + 1)]
    t.append(fib(x, array))

for i in range(1, int(input()) + 1):
    if i in t:
        print("+", end="")
    else:
        print("-", end="")
