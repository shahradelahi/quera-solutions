count, times = map(int, input().split())
nums = list(map(int, input().split()))

for i in range(times):
    nums.insert(0, nums.pop())

print(*nums)
