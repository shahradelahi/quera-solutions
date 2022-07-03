n, q = map(int, input().split())
a = list(map(int, input().split()))
for i in range(q):
    t, l, r = map(int, input().split())
    l -= 1
    r -= 1
    if t == 1:
        print(sum(a[l:r + 1]))
    else:
        t = a[r]
        for j in range(r - 1, l - 1, -1):
            a[j + 1] = a[j]
        a[l] = t
