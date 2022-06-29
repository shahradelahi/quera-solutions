number = int(input())
exponent = 2

while 2 ** exponent < number:
    exponent += 1

print(2 ** exponent)
