def power_set(arr):
    res = []
    power(arr, res, [], 0)
    return res


def power(arr, res, selected, idx):
    if idx == len(arr):
        res.append(selected[:])
        return
    power(arr, res, selected, idx + 1)
    power(arr, res, selected + [arr[idx]], idx + 1)


print(power_set([1, 2, 3]))
