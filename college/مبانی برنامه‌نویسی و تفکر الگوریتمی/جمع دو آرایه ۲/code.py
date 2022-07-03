numbers, each_row = map(int, input().split())
a, b = [], []

for i in range(numbers):
    a.append(list(map(int, input().split())))

for i in range(numbers):
    b.append(list(map(int, input().split())))

c = []

for i in range(numbers):
    r = []
    for j in range(each_row):
        r.append(a[i][j] + b[i][j])
    c.append(r)

for i in c:
    print(*i)
