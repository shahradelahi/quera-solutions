count_of_stones = int(input())
stones = []

for i in range(count_of_stones):
    stones.append(int(input()))


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def lower_prime_count(n):
    count = 0
    for i in range(1, n):
        if is_prime(i):
            count += 1
    return count


def primed_divs_count(n):
    count = 0
    for i in range(1, n):
        if is_prime(i):
            if n % i == 0:
                count += 1
    return count


over_all_price = 0

for stone in stones:
    if is_prime(stone):
        over_all_price += lower_prime_count(stone)
    else:
        over_all_price += primed_divs_count(stone)

if is_prime(over_all_price):
    over_all_price -= lower_prime_count(over_all_price)
else:
    over_all_price -= primed_divs_count(over_all_price)

print(over_all_price)
