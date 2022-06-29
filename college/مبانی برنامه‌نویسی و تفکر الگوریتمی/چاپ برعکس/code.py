lst = []
x = int(input())
while x != 0:
    lst.append(x)
    x = int(input())

lst = lst[::-1]
for i in range(len(lst)):
    print(lst[i])
