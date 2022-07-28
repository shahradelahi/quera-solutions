a, b, x = input().split()
a, b, x = int(a), int(b), int(x)
ans = 0

for i in range(1, a + 1):
    for j in range(1, b + 1):
        if a % i == 0 and b % j == 0 and i + j <= x:
            ans += 1

print(ans)

# todo: review this problem again
