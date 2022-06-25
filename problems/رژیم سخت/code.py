c1, c2, c3, c4, c5 = input()
list1 = [c1, c2, c3, c4, c5]

if list1.count("R") == 3 or list1.count("R") >= 2 and list1.count("Y") >= 2 or list1.count("G") == 0:
    print("nakhor lite")
else:
    print("rahat baash")

