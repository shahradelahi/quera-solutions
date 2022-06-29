house_width, house_height = map(int, input().split())
masud_width, masud_height = map(int, input().split())

if house_width >= masud_width and house_height >= masud_height:
    print("yes")
else:
    print("no")
