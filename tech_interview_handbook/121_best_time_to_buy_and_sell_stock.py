#Say you have an array for which the ith element is the price of a given stock on day i.
#If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#Note that you cannot sell a stock before you buy one.
#Example 1:

#Input: [7,1,5,3,6,4]
#Output: 5
#Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#             Not 7-1 = 6, as selling price needs to be larger than buying price.

#Example 2:
#Input: [7,6,4,3,1]
#Output: 0
#Explanation: In this case, no transaction is done, i.e. max profit = 0.

# going to iterate over the list once
# want to find max profit
# consider every curr_num to be smallest_num
# smallest num is always attempted to be minimized
# i.e. iteration 0 => smallest_num = 7
# iteration 1 => smallest_num = min(7, 1) => 1
# if we can minimize smallest num, minimize it and continue to the list
# if we cant, then we want to check if we can maximize our profit
# iteration 2 => smallest_num = 1, curr_num = 5
# 5 < 1? no so maximize profit; res = max(0, 5-1)

# o n time, o 1 space

def solve(stocks):
    if not stocks:
        return 0
    smallest_num = stocks[0]
    res = 0
    for stock in stocks[1:]:
        if stock < smallest_num:
            smallest_num = stock
        else:
            res = max(res, stock - smallest_num)
    return res
nums = [7,1,5,3,6,4]
print(solve(nums)) # 5
