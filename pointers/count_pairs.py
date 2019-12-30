# Count pairs with given sum
# Given an array of integers, and a number sum find the number of pairs of integers in the array whose sum is equal to sum.

# Examples:

# Input  :  arr[] = {1, 5, 7, -1},
#           sum = 6
# Output :  2
# Pairs with sum 6 are (1, 5) and (7, -1)

# Input  :  arr[] = {1, 5, 7, -1, 5},
#           sum = 6
# Output :  3
# Pairs with sum 6 are (1, 5), (7, -1) &
#                      (1, 5)

# Input  :  arr[] = {1, 1, 1, 1},
#           sum = 2
# Output :  6
# There are 3! pairs with sum 2.

# Input  :  arr[] = {10, 12, 10, 15, -1, 7, 6,
#                    5, 4, 2, 1, 1, 1},
#           sum = 11
# Output :  9


def count_pairs(arr, target):
    import collections
    hashmap = collections.defaultdict(int)
    for val in arr:
        hashmap[val] += 1
    res = 0
    for num in arr:
        num_2 = target - num
        if num_2 in hashmap:
            res += hashmap[num_2]
        if num_2 == num:
            res -= 1
    return res//2


print(count_pairs([1, 5, 7, -1], 6))
print(count_pairs([1, 1, 1, 1], 2))
print(count_pairs([10, 12, 10, 15, -1, 7, 6, 5, 4, 2, 1, 1, 1], 11))
