n, m = map(int, input().split())
a = [input() for _ in range(n)]
s = input()
size = len(s)
answer = 0

for i in range(n):
    for j in range(m - size + 1):
        difference = 0
        for k in range(size):
            if s[k] != a[i][k + j]:
                difference = 1
        if difference == 0:
            answer += 1

for i in range(n - size + 1):
    for j in range(m):
        difference = 0
        for k in range(size):
            if s[k] != a[i + k][j]:
                difference = 1
        if difference == 0:
            answer += 1

print(answer)

# todo: review this problem again
