def check(a, k, x):
    consecutive_elements = 0
    answer_exists = False
    for i in range(len(a)):
        if a[i] >= x:
            consecutive_elements += 1
        else:
            consecutive_elements = 0
        if consecutive_elements == k:
            answer_exists = True
    return answer_exists


n, k = map(int, input().split())
a = list(map(int, input().split()))

l = 0
r = 10 ** 9
while l != r:
    mid = (l + r + 1) // 2
    if check(a, k, mid):
        l = mid
    else:
        r = mid - 1
print(l)
