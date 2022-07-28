n, k = map(int, input().split())
a = list(map(int, input().split()))
for i in range(0, n):
    flag = True
    if i + k - 1 < n:
        for j in range(i + 1, i + k):
            if a[j] < a[j - 1]:
                flag = False
    else:
        flag = False
    if flag:
        print("{} to {}".format(i, i + k - 1))

# todo: review this problem again
