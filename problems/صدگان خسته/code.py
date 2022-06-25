a, b = input()[::-1], input()[::-1]

left, right = str(min(a, b))[::-1], str(max(a, b))[::-1]

if int(a) == int(b):
    print("%s = %s" % (left, right))
elif int(left[::-1]) > int(right[::-1]):
    print("%s > %s" % (left, right))
else:
    print("%s < %s" % (left, right))
