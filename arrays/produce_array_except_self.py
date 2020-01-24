# leetcode medium
# input [1, 2, 3, 4]
# output [24, 12, 8, 6]

def product(array):
    p = 1
    res = [1] * len(array)
    
    for i in range(len(array)):
        res[i] = p
        p *= array[i]
    p = 1

    for i in range(len(array) -1, -1, -1):
        res[i] *= p
        p *= array[i]
    return res

print(product([1, 2, 3, 4]))