count_of_persons, first_person = map(int, input().split())
current_person = first_person
current_person = current_person % count_of_persons
turns = 1

while current_person != 0:
    turns += 1
    current_person += first_person
    current_person = current_person % count_of_persons

print(turns)
