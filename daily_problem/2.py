# given a array of integers return a new array such that
# each element at index i of the new array is the product of all numbers
# except original array at i

# ip [1, 2, 3, 4, 5]
# op [120, 60, 40, 30, 24]

nums = input()

def solve(nums):
    res = [1] * len(nums)
    mult = 1
    for i in range(len(nums)):
        res[i] = mult
        mult *= nums[i]
    mult = 1
    for i in range(len(nums)-1,-1,-1):
        res[i] *= mult
        mult *= nums[i]
    return res
print(solve(nums))