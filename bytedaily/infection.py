# Given a 2D array each cells can have one of three values. Zero represents an empty cell, one represents a healthy person, and two represents a sick person.
# Each minute that passes, any healthy person who is adjacent to a sick person becomes sick. Return the total number of minutes that must elapse until every person is sick.
# Note: If it is not possible for each person to become sick, return -1.

# Ex: Given the following 2D array grid…

# grid = [
#     [1,1,1],
#     [1,1,0],
#     [0,1,2]
# ], return 4.
# [2, 1] becomes sick at minute 1.
# [1, 1] becomes sick at minute 2. 
# [1, 0] and [0, 1] become sick at minute 3.
# [0, 0] and [0, 2] become sick at minute 4.
# Ex: Given the following 2D array grid…

# grid = [
#     [1,1,1],
#     [0,0,0],
#     [2,0,1]
# ], return -1.

def infection(grid):
    healthy_people_amount = 0
    sick_person_locations = []
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                healthy_people_amount += 1
            elif grid[i][j] == 2:
                sick_person_locations.append((i, j))

    while sick_person_locations:
        new_sick_person_locations = []
        for i, j in sick_person_locations:
            for x, y in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                next_x, next_y = i + x, y + j
                if 0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]):
                    if grid[next_x][next_y] == 1:
                        grid[next_x][next_y] = 2
                        healthy_people_amount -= 1
                        new_sick_person_locations.append((next_x, next_y))
        sick_person_locations = new_sick_person_locations
        res += 1
    return res - 1 if healthy_people_amount == 0 else -1

grid = [
    [1,1,1],
    [0,0,0],
    [2,0,1]
]
print(infection(grid))

grid = [
    [1,1,1],
    [1,1,0],
    [0,1,2]
]
print(infection(grid))
