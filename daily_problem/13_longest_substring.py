#This problem was asked by Amazon.

#Given an integer k and a string s, find the length of the longest substring 
#that contains at most k distinct characters.

#For example, given s = "abcba" and k = 2, the longest substring with k distinct 
#characters is "bcb".

s = input()
k = input()

# "abcba"
# "a" hmap[a] = 0
# "ab" hmap[a] = 0, hmap[b] = 1
# "abc" len(hmap) > k...
# so remove the oldest key value
# we had ab
# remove a
# now we have bc
# "abcb", no repeat res = "bcb"
# "abcba", len(hmap) > k so ....
# remove lowest key value
# which will be c 
# then we have ba

def solve(s, k):
    if not s or k == 0:
        return 0
    res = ""
    hmap = {}
    start = 0
    for i, v in enumerate(s):
        if len(hmap) == k and v not in hmap:
            min_val, min_key = float("inf"), None
            for key,val in hmap.items():
                if min_val > val:
                    min_val = hmap[key]
                    min_key = key
            start = max(start, hmap[min_key] + 1)
            hmap.pop(min_key)
        res = max(res, s[start:i+1], key=len)
        hmap[v] = i
    return len(res)

print(solve(s, k))
