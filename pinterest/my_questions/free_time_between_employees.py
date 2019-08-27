# given two arrays of tuples
# find the free time between two employees schedule
# tuples = (start, end)
# i.e
# employee_1 = [ (2, 6), (54, 90) ]
# employee_2 = [ (3, 5), (43, 54), (75, 97) ]
# ans = [ (0, 2), (6, 43), (97, 100) ]

# WIP


def free_time_between_two_employees(employee_1, employee_2):
    # i think we should get the free time of both employees first...
    # rather than their work time
    employee_1.sort(key=lambda i: i[0])
    employee_2.sort(key=lambda i: i[0])

    work_overlap = []

    idx, jdx, m, n = 0, 0, len(employee_1), len(employee_2)

    while idx < m or jdx < n:
        if work_overlap and idx < m and employee_1[idx][0] <= work_overlap[-1][1]:
            last_start, last_end = work_overlap[-1]
            work_overlap[-1] = (last_start, max(last_end,
                                                work_overlap[idx][1]))
        else:
            min_num = employee_1[idx][0] if jdx >= n else min(
                employee_1[idx][0], employee_2[jdx][0])
            work_overlap.append(
                (min_num, employee_1[idx][1]))

        if work_overlap and jdx >= n and employee_2[jdx][0] <= work_overlap[-1][1]:
            last_start, last_end = work_overlap[-1]
            work_overlap[-1] = (last_start, max(last_end, employee_2[jdx][1]))
        else:
            min_num = employee_2[jdx][0] if idx >= m else min(
                employee_1[idx][0], employee_2[jdx][0])
            work_overlap.append(
                (min_num, employee_2[idx][1]))
        idx += 1
        jdx += 1
    print(work_overlap)

    # # [ (0, 2) ]
    # free_time_emp_1 = [(0, employee_1[0][0]) if employee_1[0]
    #                    [0] != 0 else (employee_1[0][1], employee_1[1][0])]
    # # [ (0, 3) ]
    # free_time_emp_2 = [(0, employee_2[0][0]) if employee_2[0]
    #                    [0] != 0 else (employee_2[0][1], employee_2[1][0])]

    # # [ (0, 2), (6, 54), (90, 100) ]
    # for start, end in employee_1:
    #     if free_time_emp_1 and free_time_emp_1[-1][1] < start:


employee_1 = [(2, 6), (54, 90)]
employee_2 = [(3, 5), (43, 54), (75, 97)]
free_time_between_two_employees(employee_1, employee_2)
