
# palindrome permutation

# given a string
# is a permutation of the stirng a palindrome?

# tact coa
# return true because it can be
# tacocat or atcocta


def palindrome_permutation(string):
    string = string.replace(" ", "")
    string = list(string)
    print(string)
    res = False
    res = recurse(res, string, 0)
    return res


def recurse(res, string, i):
    if i == len(string) - 1:
        temp = ''.join(string)
        print(temp == temp[::-1])
        if temp == temp[::-1]:
            res = True
            return res
    else:
        for j in range(i, len(string)):
            swap(i, j, string)
            res = recurse(res, string, i + 1)
            swap(i, j, string)
    return res

def swap(i, j, string):
    string[i], string[j] = string[j], string[i]


print(palindrome_permutation("tact coa"))
