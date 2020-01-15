def create_subsets(n, k):
    res = []
    rec(1, n, k, res, [])
    return res


def rec(offset, n, k, res, arr):
    if len(arr) == k:
        res.append(arr)
        return
    i = offset
    #remaining = k - len(arr)
    while i <= n:#and remaining <= n - i + 1:
        rec(i + 1, n, k, res, arr + [i])
        i += 1


print(create_subsets(5, 3))
