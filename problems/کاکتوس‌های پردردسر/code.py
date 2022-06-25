n = int(input())
x = map(int, input().split())

for i in x:
    if i <= 3:
        print("*" * i)
    else:
        print("*")
