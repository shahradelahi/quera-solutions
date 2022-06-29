cup1, cup2, cup3 = map(float, input().split())
cups = [cup1, cup2, cup3]

each_must_have = sum(cups) / len(cups)
moves = 0

for cup_index in range(len(cups)):
    for i in range(len(cups)):
        if cup_index != i and cups[cup_index] > each_must_have > cups[i]:
            have_extra = cups[cup_index] - each_must_have
            needs = each_must_have - cups[i]
            if have_extra >= needs:
                can_move = needs
            else:
                can_move = have_extra
            cups[cup_index] -= can_move
            cups[i] += can_move
            moves += 1

print(moves)
