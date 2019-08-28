Input = [4, 3, 2, 4, 1, 3, 2]
#Output: 1

# techleads sol


def singleNumber(nums):
    unique = 0

    for n in nums:
        print(bin(unique), "xor", bin(n))
        unique ^= n

    return unique


print singleNumber(Input)
