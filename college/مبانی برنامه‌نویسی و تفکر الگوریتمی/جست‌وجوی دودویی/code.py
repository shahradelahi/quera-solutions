arr = [10, 12, 25, 50, 90, 95, 100, 150, 190, 200]
target = 100

left = 0
right = len(arr)

while right - left > 1:
    mid = (left + right) // 2
    if arr[mid] <= target:
        left = mid
    elif arr[mid] > target:
        right = mid

if arr[left] == target:
    print(left)
else:
    print(-1)
