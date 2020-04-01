
# roman numerals are as follows

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

integer = input()

def solve(integer):
    hmap = {1000: "M", 900: "CM", 500:"D", 400:"CD", 100: "C", 90:"XC", 50: "L", 40:"XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1:"I"}
    vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    res = ""
    for x in vals:
        if integer >= x:
            res += hmap[x] * (integer // x)
            integer = integer % x
    return res
print(solve(integer))
