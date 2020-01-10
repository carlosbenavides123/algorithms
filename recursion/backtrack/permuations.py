def generate(arr):
    res = []
    permutation(arr, res, 0)
    return res


def permutation(arr, res, i):
    print(i)
    if i == len(arr) - 1:
        res.append(arr[:])
        return
    else:
        for j in range(i, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            print(arr[:],i, j)
            permutation(arr, res, i + 1)
            arr[i], arr[j] = arr[j], arr[i]


print(generate([2, 3, 5, 7]))
