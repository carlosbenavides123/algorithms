employees = input()

def solve(employees):
    if not employees:
        return 0
    employees = int(employees)
    res = 1
    leader = 2
    while leader <= employees / 2:
        temp = (employees-leader)%leader
        if temp == 0:
            res += 1
        leader += 1
    return res
print(solve(employees))