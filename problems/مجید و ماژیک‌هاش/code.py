n = int(input())
color = list(map(int, input().split()))
counter = [0] * (max(color) + 1)

for i in range(n):
    counter[color[i]] += 1

max_color = 0
for i in range(len(counter)):
    if counter[i] > 0 and i > max_color:
        max_color = i

answer = -1
for i in range(1, max_color + 1):
    if counter[i] > 0:
        if answer == -1 or counter[answer] > counter[i] or (counter[answer] == counter[i] and i < answer):
            answer = i

print(answer)
