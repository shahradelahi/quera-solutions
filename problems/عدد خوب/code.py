def num_divs(target):
    divs = 0
    counter = 1
    while counter <= target:
        if target % counter == 0:
            divs += 1
        counter += 1
    return divs


def good_num(number):
    return (number * (number + 1)) // 2


n = int(input())

answer = 1
while num_divs(good_num(answer)) < n:
    answer += 1

print(good_num(answer))
