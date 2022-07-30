n, x, y = map(int, input().split())

for i in range(n // x + 1):
    if (n - i * x) % y == 0:
        print(i, (n - i * x) // y)
        break
else:
    print(-1)

# todo: review this problem again
