
nums = [int(num) for num in input().split()]

def solve(nums):
    nums = sorted(nums)
    c = (nums[0]+nums[1]) - nums[3]
    b = (nums[0]+nums[2]) - nums[3]
    a = (nums[1]+nums[2]) - nums[3]
    return a, b, c
sol = solve(nums)
for item in sol:
    print(item)