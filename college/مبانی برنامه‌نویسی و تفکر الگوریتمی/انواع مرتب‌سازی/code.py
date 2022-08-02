def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i, len(lst)):
            if lst[min_index] > lst[j]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst


def bubble_sort(lst):
    for i in range(1, len(lst)):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def insertion_sort(lst):
    for i in range(1, len(lst)):
        p = i
        while p > 0 and lst[p] < lst[p - 1]:
            lst[p], lst[p - 1] = lst[p - 1], lst[p]
            p -= 1
    return lst


numbers = [5, 2, 4, 6, 1, 3]

print("SelectionSort: ", selection_sort(numbers))
print("BubbleSort: ", bubble_sort(numbers))
print("InsertionSort: ", insertion_sort(numbers))
