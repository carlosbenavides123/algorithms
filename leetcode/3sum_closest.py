# given nums return the closest 3 nums to the num

num = input()
nums = [int(x) for x in input().split()]

def solve(target, nums):
    nums = sorted(nums)
    res = sum(nums[:3])
    
    for i in range(len(nums)-1):
        l = i + 1
        r = len(nums) - 1
        while l < r:
            curr_val = nums[i] + nums[l] + nums[r]
            if abs(curr_val - target) < abs(res - target):
                res = curr_val
            elif curr_val < target:
                l += 1
            elif curr_val > target:
                r -= 1
            else:
                break
    return res
            
print(solve(num, nums))
            