# This problem was asked by Coinbase.

# Write a function that takes in a number, 
# string, list, or dictionary and returns its JSON encoding. It should also handle nulls.

# For example, given the following input:

# [None, 123, ["a", "b"], {"c":"d"}]
# You should return the following, as a string:

# '[null, 123, ["a", "b"], {"c": "d"}]'

def json_encode(obj):
    if obj is None:
        return "null"
    if isinstance(obj, str):
        return '"' + obj + '"'
    if isinstance(obj, int):
        return str(obj)
    if isinstance(obj, list):
        s = ', '.join([json_encode(o) for o in obj])
        return '[' + s + ']'
    if isinstance(obj, dict):
        if len(obj) == 0:
            return "{}"
        jsonified = []
        for k, v in obj.items():
            jsonified.append(json_encode(k) + ': ' + json_encode(v))
        return '{' + ', '.join(jsonified) + '}'


obj = [None, 123, ["a", "b"], {"c":"d"}]
obj = {"key": "value", "date": {"year": 2020, "month": "September", "day": 17}}
print(json_encode(obj))

def pretty_print(json):
    if not json:
        return ''
    
    result = []
    multiplier = 0
    i = 0
    
    while i < len(json):
        if json[i] in ['{', '[']:
            result.append('  ' * multiplier + json[i])
            multiplier += 1
            i += 1
        elif json[i] in ['}', ']']:
            multiplier -= 1
            result.append('  ' * multiplier + json[i])
            i += 1
        elif json[i] == ',':
            result[-1]+= ','
            i += 1
        else:
            start = i
            while i < len(json) and json[i] not in ['{', '}', ',', '[', ']']:
                i += 1
            curr_s = json[start:i]
            result.append('  ' * multiplier + curr_s)
    
    for r in result:
        print(r)




# Given an array arr[] consisting of 0’s and 1’s. A flip operation is one in which you turn 1 into 0 and a 0 into 1.You have to do atmost one “Flip” operation of a subarray. Then finally display maximum number of 1 you can have in the array.

# Input:
# The first line of input consist of a single integer T denoting the total number of test case. First line of test case contains an integer N size of array. Second line of test case contains N space separated integers denoting the array arr[].

# Output:
# For each test case output a single integer representing  the maximum number of 1's you can have in the array after atmost one flip operation.

# Constraints:
# 1 <= T = 100
# 1 <= N <= 104
# 0 <= arr[i] <= 1

# Example:
# Input:
# 1
# 5
# 1 0 0 1 0 

# Output:
# 4

# Explanation:
# We can perform a flip operation in the range [1,2]
# After flip operation array is : 1 1 1 1 0

def flip_bits(bits):
    max_score = 0
    score = 0
    temp_l = 0
    l = 0
    r = 0
    res = 0
    while r < len(bits):
        if bits[r] == 0: score += 1
        else: score -= 1
        if max_score < score:
            max_score = score
            l = temp_l
            res = max(res, r - l)
        if score < 0:
            score = 0
            temp_l = r
        r += 1
    res = max(res, r - l)
    return res
print(flip_bits([0, 0, 1, 1, 1]))





def isMatch(self, s: str, p: str) -> bool:
    dp = [[False for y in range(len(p) + 1)] for x in range(len(s) + 1)]
    dp[0][0] = True
    for i in range(1, len(p) + 1):
        if p[i-1] == "*":
            dp[0][i] = True
        else:
            break

    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if s[i-1] == p[j-1] or p[j-1] == "?":
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == "*":
                dp[i][j] = dp[i-1][j] or dp[i-1][j-1] or dp[i][j-1]
    return dp[-1][-1]

