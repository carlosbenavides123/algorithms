# Given a sorted list of numbers, and two integers
# low and high representing the lower and upper bound of a range,
# return a list of(inclusive) ranges where the numbers are missing.
# A range should be represented by a tuple in the format of(lower, upper).

# Here's an example and some starting code:


def missing_ranges(nums, low, high):
    # Fill this in.
    res = []
    if low < nums[0] - 1:
        res.append((low, nums[0]-1))
    for i in range(len(nums)-1):
        curr_num = nums[i]
        next_num = nums[i+1]
        if curr_num + 1 == next_num:
            continue
        res.append((curr_num + 1, next_num - 1))
        if high > nums[len(nums) - 1]:
            res.append((nums[len(nums) - 1]), high)
    return res


print(missing_ranges([1, 3, 5, 10], 1, 10))
# [(2, 2), (4, 4), (6, 9)]
