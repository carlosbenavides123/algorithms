def generate_paran(n):
    res = []
    strlen = n * 2
    rec(strlen, res, "", n, n)
    return res


def rec(strlen, res, string, left, right):
    if len(string) == strlen:
        res.append(string)
        return
    if left > 0:
        rec(strlen, res, string + "(", left - 1, right)
    if left < right:
        rec(strlen, res, string + ")", left, right - 1)


print(generate_paran(3))
