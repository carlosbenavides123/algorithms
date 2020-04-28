
# Given a list of nums, find two nums that add up to a target
nums = input()
target = input()

def solve(nums, target):
    hmap = {}
    for i in range(len(nums)):
        if nums[i] in hmap:
            return [hmap[nums[i]], nums[i]]
        key = target-nums[i]
        hmap[key] = nums[i]
    return [-1, -1]
print(solve(nums, target)) 
        