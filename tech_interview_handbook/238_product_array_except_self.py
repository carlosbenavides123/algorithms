#Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

#Example:

#Input:  [1,2,3,4]
#Output: [24,12,8,6]
#Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

#Note: Please solve it without division and in O(n).

#Follow up:
#Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

# have a var, multiplier than multiplies itself with curr val
# so var multiplier = 1
# initialize a res_arr to be [1]*len(arr)
# iteratve over the input
# res_arr.append(curr_num * multiplier)
# multiplier = multiplier * curr_num
# iter 1 -> 1
# iter 2 -> 2
# iter 3 -> 6
# iter 4 -> 24 (we never use the last one as we multiply and append before updating multiplier variable)
# we want to see
# [1, 1, 2, 6]
# then we iterate reverse
# so that we can see [24, 12, 8, 6]
# using the same logic

def solve(nums):
    multiplier = 1
    res = [1] * len(nums)
    for i, num in enumerate(nums):
        res[i] = multiplier
        multiplier = multiplier * num
    multiplier = 1
    for i in range(len(nums) -1, -1, -1):
        num = nums[i]
        res[i] = res[i] * multiplier
        multiplier = multiplier * num
    return res
nums = [1, 2, 3, 4]
print(solve(nums))
