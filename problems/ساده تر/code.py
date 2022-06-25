nums = []

for i in range(1, 5):
    nums.append(int(input()))

print("Sum : %.6f" % sum(nums))
print("Average : %.6f" % (sum(nums) / len(nums)))
print("Product : %.6f" % (nums[0] * nums[1] * nums[2] * nums[3]))
print("Max : %.6f" % max(nums))
print("Min : %.6f" % min(nums))
