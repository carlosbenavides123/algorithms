# Give an array of salaries. The total salary has a budget. At the beginning, the
# total salary of employees is larger than the budget. It is required to find the number k,
#  and reduce all the salaries larger than k to k, such that the total salary is exactly equal to the budget.

# Example 1:

# Input: salaries = [100, 300, 200, 400], budget = 800
# Output: 250
# Explanation: k should be 250, so the total salary after the reduction 100 + 250 + 200 + 250
# is exactly equal to 800.
# You can assume that solution always exists.


def adjust_salaries(salaries, budget):
    left = min(salaries)
    right = max(salaries)

    while left < right:
        k = (left + right) // 2
        total_spent = calculate_budget(salaries, budget, k)
        if total_spent == budget:
            return k
        if total_spent < budget:
            left = k
        else:
            right = k
        print(k)
    return k


def calculate_budget(salaries, budget, k):
    idx = 0
    total_spent = 0
    while idx < len(salaries):
        salary = salaries[idx]
        if salary > k:
            salary = k
        total_spent += salary
        idx += 1
    return total_spent


print(adjust_salaries([100, 300, 200, 400], 750))
