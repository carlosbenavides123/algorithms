# given n non-negative integers, each index in a array represents a height of a pillar
# given this, find the largest area
# length of array is atleast 2

nums = input()

def solve(nums):
    res = 0
    l = 0
    r = len(nums) - 1
    while l < r:
        h = min(nums[l], nums[r])
        res = max(res, h * (r-l))
        if nums[l] < nums[r]:
            l += 1
        else:
            r -= 1
    return res

print(solve(nums))