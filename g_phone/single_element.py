# Given an array nums of length n.
# All elements appear in pairs except one of them.
# Find this single element that appears alone.
# Pairs of the same element cannot be adjacent:

# [2, 2, 1, 2, 2] // ok
# [2, 2, 2, 2, 1] // not allowed

# Input: [2, 2, 1, 1, 9, 9, 5, 2, 2]
# Output: 5

# xor O(n) time O(1) space


def single_element(nums):
    res = 0
    for num in nums:
        res ^= num
    return res


print(single_element([2, 2, 2, 2, 1]))

# follow up, can you do better than O(n)?
# Input: [2, 2, 1, 1, 9, 9, 5, 2, 2]
# len nums = 9
# mid = 4


def single_element(A):
    if len(A) == 1:
        return A[0]
    if A[0] != A[1]:
        return A[0]
    if A[-1] != A[-2]:
        return A[-1]

    l, h = 0, len(A)
    while l < h:
        m = (l + h) // 2
        print(m, A[m], A[m+1])
        if A[m] not in [A[m - 1], A[m + 1]]:
            return A[m]
        elif m % 2:
            if A[m] == A[m + 1]:
                h = m
            else:
                l = m
        else:
            if A[m] == A[m + 1]:
                l = m
            else:
                h = m


print(single_element([2, 2, 3, 1, 1, 7, 7, 9, 9]))
