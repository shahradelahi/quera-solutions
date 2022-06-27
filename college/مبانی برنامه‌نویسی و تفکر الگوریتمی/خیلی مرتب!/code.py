def is_even(x):
    print("Zoj")
    print(x + 2)


def is_odd(x):
    print("Fard")
    print(x + 1)


def even_or_odd(x):
    if x % 2 == 0:
        is_even(x)
    else:
        is_odd(x)


number = int(input())
even_or_odd(number)
