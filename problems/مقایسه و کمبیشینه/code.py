a, b, c = input().split()
x, y, z = map(int, input().split())

if a == b:
    print("Max : %d" % max(x, y, z))
elif a == c:
    print("Min : %d" % min(x, y, z))
else:
    print("None")
