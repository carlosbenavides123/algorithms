# Given an integer array nums containing positive elements and an int maxValue.
# Find the value of x such that the sum of the elements of the array is
# maximum and is less than the given maxValue. x is defined as:
# if the current value is greater than x, then x is used as the new value,
# otherwise keep the original value nums[i] = min(x, nums[i]).

# Example 1:

# Input: nums = [10, 5, 20, 30], maxValue = 40
# Output: 12
# Explanation:
# If x = 10, the array would be nums = [10, 5, 10, 10] and the sum of the array elements would be 35.
# If x = 12, the array would be nums = [10, 5, 12, 12] and the sum of the elements would be 39 which is the maximum sum close to given maxValue which is 40.
# So the answer would be 12.


def array_adjustment(nums, target):
    left = min(nums)
    right = max(nums)

    while left < right:
        x = (left + right) // 2
        new_num = calculate_new_nums(nums, x)
        print(x, new_num)
        if new_num == target:
            return x
        if new_num < target:
            left = x + 1
        else:
            right = x
    return x


def calculate_new_nums(nums, x):
    total = 0
    idx = 0
    while idx < len(nums):
        num = nums[idx]
        if num > x:
            num = x
        total += num
        idx += 1
    return total


print(array_adjustment([10, 5, 20, 30], 40))
