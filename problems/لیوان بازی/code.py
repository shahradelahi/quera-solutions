count_of_moves, first_place = input().split()

position = first_place
for i in range(int(count_of_moves)):
    new_position, last_position = input().split()

    if position == last_position:
        position = new_position
    elif position == new_position:
        position = last_position

print(position)
