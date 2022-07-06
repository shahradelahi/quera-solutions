count_of_letters = int(input())
first_word = input()
second_word = input()
counter = 0

for i in range(count_of_letters):
    if first_word[i] != second_word[i]:
        counter += 1

print(counter)
