# given two sorted arrays, find the median
# overall should ruin around O(log(m+n))

import heapq

nums1 = input("input array1\n")
nums2 = input("input array2\n")

def median_of_two(nums1, nums2):
    arr1, arr2 = sorted((nums1, nums2), key=len)
    m, n = len(arr1), len(arr2)
    l, h = 0, m

    while l <= h:
        i = (l + h)/2
        j = (m+n)/2-i

        max_left_side_A = arr1[i-1] if i>0 else float("-inf")
        max_left_side_B = arr2[j-1] if j>0 else float("-inf")

        min_right_side_A = arr1[i] if m-i>0 else float("inf")
        min_right_side_B = arr2[j] if n-j>0 else float("inf")

        print(max_left_side_A, max_left_side_B)
        print(min_right_side_A, min_right_side_B)

        if max_left_side_A <= min_right_side_B and max_left_side_B <= min_right_side_A:
            if (m+n) % 2 == 1:
                return min(min_right_side_A, min_right_side_B)
            else:
                return (max(max_left_side_A, max_left_side_B) + min(min_right_side_A, min_right_side_B))/2.0
        elif max_left_side_A > min_right_side_B:
            h = i - 1
        else:
            l = i + 1
    return -1
print(median_of_two(nums1, nums2))
