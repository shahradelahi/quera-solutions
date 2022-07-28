count_of_actions = int(input())
collector = {}

for i in range(count_of_actions):
    aType, aValue = input().split()
    aValue = int(aValue)

    if aValue not in collector:
        collector[aValue] = 0

    if aType == '?':
        print(collector[aValue])
    else:
        collector[aValue] += 1
