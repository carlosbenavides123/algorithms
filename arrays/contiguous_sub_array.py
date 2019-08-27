def max_subarray_sum(arr):
    l, r = -1, 0
    res = [0, 0]
    maxSoFar = float("-inf")
    while l <= r and l < len(arr) and r < len(arr):
        if arr[r] < 0:
            l += 1
            r += 1
        else:
            r += 1
        print(r)
        print(l)
        if maxSoFar < sum(arr[l:r+1]):
            maxSoFar = sum(arr[l:r+1])
            res = [l, r]
        print(l, r)
    return [arr[i] for i in range(l+1, r)]


print max_subarray_sum([34, -50, 42, 14, -5, 86])
# 137
# [42, 14, -5, 86].
