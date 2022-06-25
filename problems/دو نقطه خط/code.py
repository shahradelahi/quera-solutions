mosiX, mosiY, bossX, bossY = map(int, input().split())

if mosiX == bossX:
    print("Vertical")
elif mosiY == bossY:
    print("Horizontal")
else:
    print("Try again")
