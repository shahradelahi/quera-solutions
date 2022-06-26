def gcd(a, b):
    if a > b:
        a, b = b, a
    while a > 0:
        b = b % a
        a, b = b, a
    return b


def lcm(a, b):
    return a * b // gcd(a, b)


number = int(input())
answer = 1

for i in range(1, number):
    if gcd(i, number) == 1:
        answer = lcm(answer, i)

print(answer)
