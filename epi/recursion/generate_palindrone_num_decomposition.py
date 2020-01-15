def generate_palind(num):
    num = str(num)
    res = []
    rec(num, res, 0, [])
    return res


def rec(num, res, offset, arr):
    if offset == len(num):
        res.append(arr)
        return
    for i in range(offset + 1, len(num) + 1):
        prefix = num[offset:i]
        if prefix == prefix[::-1]:
            rec(num, res, i, arr + [prefix])


def expand_palind(num, l, r):
    while l > -1 and r < len(num) and num[l] == num[r]:
        l -= 1
        r += 1
    return num[l+1:r]


print(generate_palind("0204451881"))
