
n = input()

def solve(n):
    res = []
    
    def recurse(l, r, n, string):
        if len(string) == n * 2:
            res.append(string)
            return
        if l < n:
            recurse(l + 1, r, n, string + "(" )
        if r < l:
            recurse(l, r + 1, n, string + ")")
    recurse(0, 0, n, "")
    return res
print(solve(n))
            