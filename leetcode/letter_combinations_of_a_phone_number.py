#given a string 2 to 9 inclusive
# return all possible numbers

num = input()

def solve(num):
    arr = ["", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    res = []
    
    def recurse(string, num):
        if not num:
            print(string)
            res.append(string)
            return
        idx = int(num[0])
        for letter in arr[idx-1]:
            recurse(string + letter, num[1:])
    recurse("", num)
    return res
print(solve(num))
