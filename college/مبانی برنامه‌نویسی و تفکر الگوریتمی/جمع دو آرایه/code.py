def merge_list(list1, list2):
    list3 = []
    for i in range(len(list1)):
        list3.append(list1[i] + list2[i])

    return list3


input()
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

print(*merge_list(l1, l2))
