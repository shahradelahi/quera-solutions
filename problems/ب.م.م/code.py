def gcd(a, b):
    if a > b:
        a, b = b, a
    while a > 0:
        b = b % a
        a, b = b, a
    return b


num1, num2 = int(input()), int(input())

print(gcd(num1, num2))
