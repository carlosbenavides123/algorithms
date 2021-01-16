# Given an unsorted integer array nums, find the smallest missing positive integer.

# Follow up: Could you implement an algorithm that runs in O(n) time and uses constant extra space.?

# i = 0
# [3, 2, 4, 56, 2, -1, 0, 2, 1]
# put 3 in 3rd slot
# [4, 2, 3, 56, 2, -1, 0, 2, 1]
# put 4 in 4th slot
# [56, 2, 3, 4, 2, -1, 0, 2, 1]

# i = 1...
# keep 2 in same slot
# keep 3 in same slot
# ignore 56
# keep 2 in same slot
# ignore -1
# ignore 0
# keep 2 in same slot
# swap 1 and 4

def first_missing_positive(nums):
    for i in range(len(nums)):
        while i + 1 != nums[i] and 0 < nums[i] < len(nums):
            nums_val_idx = nums[i]
            if nums[nums_val_idx - 1] == nums[i]:
                break
            nums[nums_val_idx-1], nums[i] = nums[i], nums[nums_val_idx-1]
    print("semi sorted", nums)
    res = 1
    for num in nums:
        if res == num:
            res += 1
    return res

# Example 1:

# Input: nums = [1,2,0]
# Output: 3
# Example 2:

# Input: nums = 
# Output: 2
# Example 3:
nums = [3, 2, 4, 56, 2, -1, 0, 2, 1]
print(first_missing_positive(nums))
# Input: nums = [7,8,9,11,12]
# Output: 1