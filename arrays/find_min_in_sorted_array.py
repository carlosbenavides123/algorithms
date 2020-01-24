#leetcode medium

# given [4, 5, 6, 7, 0, 1, 2]
# return 0

def min_in_shifted_sorted_arr(arr):
    l = 0
    r = len(arr) - 1

    while l < r:
        mid = (l + r) // 2

        if arr[mid] > arr[r]:
            l = mid + 1
        else:
            r = mid
    return arr[l]

print(min_in_shifted_sorted_arr([4, 5, 6, 7, 0, 1, 2]))