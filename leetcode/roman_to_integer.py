# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

roman = input()

def solve(roman):
    res = 0
    index = 0
    hmap = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    while index < len(roman):
        if index + 1 < len(roman) and hmap[roman[index]] < hmap[roman[index+1]]:
            res += hmap[roman[index+1]] - hmap[roman[index]]
            index += 1
        else:
            res += hmap[roman[index]]
        index += 1
    return res
print(solve(roman))
            
            