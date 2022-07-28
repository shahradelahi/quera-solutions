def unique_chars(string):
    lst = []
    for x in string:
        if x not in lst:
            lst.append(x)
    return len(lst)


count = int(input())
collector = []

for i in range(count):
    collector.append(unique_chars(input()))

print(max(collector))
