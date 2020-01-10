# import math
# from math import gcd

from fractions import gcd


def enigma(rC, minRV, maxRV):
    def rec(curr, count, out):
        if count == rC:
            out += curr,
            return
        for i in range(minRV, maxRV+1):
            if not curr:
                rec([i], count+1, out)
            elif curr:
                if gcd(i, curr[0]) == 1:
                    rec(curr+[i], count+1, out)

    out = []
    rec([], 0, out)
    return out


print(enigma(3, 2, 4))
