n, k = list(map(int, input().split()))
names = [input() for name in range(n)]

res = {}
for name in names:
    res[name[:k]] = res.get(name[:k], 0) + 1

print(max(list(res.values())))
