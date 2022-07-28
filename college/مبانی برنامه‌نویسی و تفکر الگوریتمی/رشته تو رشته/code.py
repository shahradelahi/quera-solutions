main = input()
key = input()
collector = []

for i in range(len(main)):
    flag = True
    for j in range(len(key)):
        if i + j < len(main):
            if main[i + j] != key[j]:
                flag = False
        else:
            flag = False
    if flag:
        collector.append(i + 1)

print(*collector)
