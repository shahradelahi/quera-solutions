from itertools import permutations

number = input()
digits = list(map(int, number))
large_numbers = []

for generation in list(permutations(digits, len(digits))):
    new_number = int(''.join(map(str, generation)))
    if int(number) < new_number:
        large_numbers.append(new_number)

if len(large_numbers) == 0:
    print(0)
else:
    print(min(large_numbers))
