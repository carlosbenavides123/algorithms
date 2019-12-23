# Find maximum (or minimum) sum of a subarray of size k
# Given an array of integers and a number k, find maximum sum of a subarray of size k.

# Examples :

# Input  : arr[] = {100, 200, 300, 400}
#          k = 2
# Output : 700

# Input  : arr[] = {1, 4, 2, 10, 23, 3, 1, 0, 20}
#          k = 4
# Output : 39
# We get maximum sum by adding subarray {4, 2, 10, 23}
# of size 4.

# Input  : arr[] = {2, 3}
#          k = 3
# Output : Invalid
# There is no subarray of size 3 as size of whole
# array is 2.


def sliding_window(array, k):
    if k > len(array):
        return -1

    left = right = 0
    res = 0

    for i in range(len(array)):
        right = i

        if k <= right:
            res = max(res + array[right] - array[left], res)
            left += 1
        else:
            res = max(res + array[right], res)

    return res


print(sliding_window([1, 4, 2, 10, 23, 3, 1, 0, 20], 4))
