count_of_actions = int(input())
lst = []

for i in range(count_of_actions):
    data = input().split()

    if data[0] == '+':
        lst.insert(int(data[1]) - 1, int(data[2]))
    if data[0] == '-':
        lst.pop(int(data[1]) - 1)

    if len(lst) == 0:
        print("EMPTY")
    else:
        print(*lst)
