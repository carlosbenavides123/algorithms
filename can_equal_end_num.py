# Given a starting number and ending number and an array of numbers.
# Return true or false if we can add/substract/multiple/divide to the starting
# number that will result in the ending number. The numbers can not be used twice.

# Start = 0, End = 10 nums [1, 2, 4, 9]  

# 1 + 9 = 10 
# return True

def can_equal_end_num(start, end, nums):
    print(start)
    if end == start: return True
    if end < start: return False

    for i in range(len(nums)):
        if can_equal_end_num(start + nums[i], end, nums[:i] + nums[i+1:]):
            return True
        if can_equal_end_num(start - nums[i], end, nums[:i] + nums[i+1:]):
            return True
        if can_equal_end_num(start * nums[i], end, nums[:i] + nums[i+1:]):
            return True
        if can_equal_end_num(start // nums[i], end, nums[:i] + nums[i+1:]):
            return True
    return False

print(can_equal_end_num(0, 73, [1, 2, 4, 9]))
