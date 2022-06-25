from_a = int(input())
to_z = int(input())


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


for number in range(from_a, to_z + 1):
    if is_prime(number):
        print(number)
