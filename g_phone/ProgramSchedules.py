# Given a sorted list of already scheduled programs and a list of new programs,
# write an algorithm to find if the given new programs can be scheduled or not?
# Each program is a pair of values where 1st value is the starting time
# and 2nd is the execution time.

# Example 1:

# Input: scheduled = [P1(10, 5), P2(25, 15)], newPrograms = [P3(18, 7), P4(12, 10)]
# Output: [true, false]
# Explanation: P3(18, 7) starts at time 18 and executes for 7 mins i.e., the end time is 18 + 7 = 25.
# So this time slot is free and there is no overlap with already scheduled programs.
# Hence P3 can be scheduled.
# As the P4 overlaps with P1, so P4 cannot be scheduled.
# Example 2:

# Input: scheduled = [P1(10, 5), P2(25, 15)], newPrograms = [P3(18, 7), P4(20, 2)]
# Output: [true, false]
# Explanation: P3 can be scheduled so we add it to already scheduled programs.
# P4 overlaps with P3, so P4 cannot be scheduled.
