n, t = input().split()
n = int(n)

for i in range(n):
    s = input()

    fail = False
    for s_char in s:
        flag = False
        for t_char in t:
            if s_char == t_char:
                flag = True

        if not flag:
            fail = True

    for t_char in t:
        flag = False
        for s_char in s:
            if s_char == t_char:
                flag = True

        if not flag:
            fail = True

    if fail:
        print("No\n")
    else:
        print("Yes\n")
