# Given a 2D matrix nums, return the matrix transposed.
# Note: The transpose of a matrix is an operation that flips each value in the matrix across its main diagonal.

# Ex: Given the following matrix nums…

# nums = [
#   [1, 2],
#   [3, 4]
# ]
# return a matrix that looks as follows...
# [
#   [1,3],
#   [2,4]
# ]

def switcheroo(nums):
    res = [[0 for y in range(len(nums))] for x in range(len(nums[0]))]
    for i in range(len(nums[0])):
        for j in range(len(nums)):
            res[j][i] = nums[i][j]
    return res

nums = [ [1, 2], [3, 4] ]
print(switcheroo(nums))

nums = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
print(switcheroo(nums))
# nums = [
#   [1, 2, 3],
#   [3, 5, 6],
#   [7, 8, 9]
# ]

# nums = [
#   [1, 4, 7],
#   [2, 5, 8],
#   [3, 6, 9]
# ]