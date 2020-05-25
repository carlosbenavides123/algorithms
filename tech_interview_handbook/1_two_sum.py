#Given an array of integers, return indices of the two numbers such that they add up to a specific target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#Example:

#Given nums = [2, 7, 11, 15], target = 9,

#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].

# 2 + 7 = 9
# positions 0 and 1
# can do double for loop
# i == 0, j == 1
# does nums[i] + nums[j] == target? if yes return
# o n^2 time o 1 space
# can use hash map
# iterating over the list once
# here we want 2 + 7
# so we can put a reminder of our 2 position
# we can say 9 - 2 = represents 7
# and using 7 we can remind ourselves of the 2 position
# so if curr_num in hmap
# return hmap[curr_num], current_index
# where hmap[curr_num], curr_num = 7, which hmap[curr_num] = 0 (position number 2)

def solve(nums, target):
    hmap = {}
    for i, num in enumerate(nums):
        if num in hmap:
            return [hmap[num], i]
        hmap[target-num] = i
    return [-1. -1]

nums = [1, 2, 3, 4, 5]
target = 6
print(solve(nums, target))
