# given two arrays of tuples
# find the free time between two employees schedule
# tuples = (start, end)
# i.e
# employee_1 = [ (2, 6), (54, 90) ]
# employee_2 = [ (3, 5), (43, 54), (75, 97) ]
# ans = [ (0, 2), (6, 43), (97, 100) ]

# nlogn time n space


def free_time_between_two_employees(employee_1, employee_2):
    # i think take all the values in both arrays, sort them by start time
    employees_work = employee_1[:] + employee_2[:]
    employees_work.sort(key=lambda i: i[0])

    merged_employee_work_time = []

    for start, end in employees_work:
        if merged_employee_work_time and start <= merged_employee_work_time[-1][1]:
            last_start, last_end = merged_employee_work_time[-1]
            merged_employee_work_time[-1] = (last_start, max(last_end, end))
        else:
            merged_employee_work_time.append((start, end))

    free_time = []

    # kinda janky way to get solution, need to find better way...
    for i in range(len(merged_employee_work_time)):
        if i == 0:
            free_time.append((0, merged_employee_work_time[i][0]))
        else:
            free_time.append(
                (merged_employee_work_time[i-1][1], merged_employee_work_time[i][0]))
    free_time.append(
        (merged_employee_work_time[-1][1], 100))

    # free_time[-1][1] = 100
    return free_time


employee_1 = [(2, 6), (54, 90)]
employee_2 = [(3, 5), (43, 54), (75, 97)]
print free_time_between_two_employees(employee_1, employee_2)
