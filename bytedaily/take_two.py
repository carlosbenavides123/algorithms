# Given an array of integers, nums, each element in the array either appears once or twice. Return a list containing all the numbers that appear twice.
# Note: Each element in nums is between one and nums.length (inclusive).

# Ex: Given the following array nums…

# nums = [2, 3, 1, 5, 5], return [5].
# Ex: Given the following array nums…

# nums = [1, 2, 3], return [].
# Ex: Given the following array nums…

# nums = [7, 2, 2, 3, 3, 4, 4], return [2,3,4].

# could use a set O(n) time and space

# could achieve O(1) space
# 
# 1 2 3 5 5
# [5]

def take_two(nums):
    dupes = []
    for i in range(len(nums)):
        idx = abs(nums[i]) - 1
        if nums[idx] < 0:
            dupes.append(abs(idx + 1))
        nums[idx] = -nums[idx]
        print(nums)
    print("final nuims", nums)
    return dupes
nums = [2, 3, 1, 5, 5]
print(take_two(nums))

# nums = [1, 2, 3]
# print(take_two(nums))

# nums = [7, 2, 2, 3, 3, 4, 4]
# print(take_two(nums))
