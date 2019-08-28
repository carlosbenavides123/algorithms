# This problem was recently asked by Uber:

# You have a landscape, in which puddles can form. You are given an array of non-negative integers representing the elevation at each location. Return the amount of water that would accumulate if it rains.

# For example: [0,1,0,2,1,0,1,3,2,1,2,1] should return 6 because 6 units of water can get trapped here.
#        X
#    XWWWXXWX
#  XWXXWXXXXXX
# # [0,1,0,2,1,0,1,3,2,1,2,1]
# Here's your starting pont:

# O(n) time space


def capacity(arr):
    # just get the max of left to right, then right to left
    # get the min of left to right, and right to left and subtract it by
    # arr[i]

    left_to_right = [0 for x in range(len(arr))]
    right_to_left = [0 for x in range(len(arr))]

    maxRainSoFar = float("-inf")
    idx = 0
    for rain in arr:
        maxRainSoFar = max(maxRainSoFar, rain)
        left_to_right[idx] = maxRainSoFar
        idx += 1

    idx -= 1
    maxRainSoFar = float("-inf")
    for rain in reversed(arr):
        maxRainSoFar = max(maxRainSoFar, rain)
        right_to_left[idx] = maxRainSoFar
        idx -= 1

    res = 0
    for rain in arr:
        rain_min_here = min(left_to_right[idx], right_to_left[idx])
        res += rain_min_here - rain
        idx += 1

    return res


print capacity([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
