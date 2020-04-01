# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:

# P     I    N
# A   L S  I G
# Y A   H R
# P     I

str = input()
rows = input()

def zigzag(s, numRows):
    step = (numRows == 1) - 1  # 0 or -1  
    res, idx = ['']*numRows, 0
    for char in s:
        res[idx] += char
        if idx == 0 or idx == numRows-1:
            step = -step
        idx += step
    return "".join(res)
print(zigzag(str, rows))