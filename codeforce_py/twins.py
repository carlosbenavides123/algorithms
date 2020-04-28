num = input()
nums = [int(x) for x in input().split()]

def solve(num, nums):
    if not num or not nums:
        return 0
    _sum = 0
    nums = sorted(nums)
    total = sum(nums)
    res = 0
    for i in range(len(nums)-1, -1, -1):
        if _sum > total / 2:
            break
        _sum += nums[i]
        res += 1
    return res
print(solve(num, nums))
        