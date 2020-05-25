#Given an array of integers, find if the array contains any duplicates.

#Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

#Example 1:
#Input: [1,2,3,1]
#Output: true

#Example 2:
#Input: [1,2,3,4]
#Output: false

#Example 3:
#Input: [1,1,1,3,3,4,3,2,4,2]
#Output: true

# o n time o n space
def solve(nums):
    hmap = {}
    for num in nums:
        if num in hmap:
            hmap[num] += 1
        else:
            hmap[num] = 1
    for num in nums:
        if hmap[num] >= 2:
            return True
    return False
nums = [1,1,1,3,3,4,3,2,4,2]
print(solve(nums))