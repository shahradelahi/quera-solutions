from functools import reduce

count = int(input())
numbers = list(map(int, input().split()))
unique_numbers = [numbers[i] for i in range(count) if numbers.count(numbers[i]) == 1]

if len(unique_numbers) < 1:
    print(0)
else:
    print(reduce(lambda x, y: x ^ y, unique_numbers))
