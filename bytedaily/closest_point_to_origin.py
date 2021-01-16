# Given a list of points, return the k closest points to the origin (0, 0).

# Ex: Given the following points and value of k…

# points = [[1,1],[-2,-2]], k = 1, return [[1, 1]].
# Thanks,
# The Daily Byte
import math
def closest_point(origin, points, k):
    if not points or not origin:
        return []
    result = points[0]
    computed_distance_values = [[distance_formula(origin, point), point] for point in points]
    computed_distance_values.sort()
    print(computed_distance_values)
    result = [point for _, point in computed_distance_values[:k]]
    return result

def distance_formula(origin, point):
    return abs((origin[0] - point[0]) ** 2 + (origin[1] - point[1]) ** 2) ** 0.5

# P = point
# Q = point and origin
# X = neither

# 1  X Q X
# 0  X X X
# -1 X X X
# -2 X X P

# use dist formula, compute each point relative to point
# sort by computed value
# return k results

origin = (0, 0)
points = [[1, 1], [-2, -2], [10, 10], [1, 0], [0, 1], [-2, 1], [2, 0]]
k = 3
print(closest_point(origin, points, k))

# lookinto this sol later

def kClosest(points, K):
    sort(points, 0, len(points)-1, K)
    return points[:K]

def sort(points, l, r, K):
    if l < r:
        p = partition(points, l, r)
        if p == K:
            return
        elif p < K:
            sort(points, p+1, r, K)
        else:
            sort(points, l, p-1, K)
        
def partition(points, l, r):
    pivot = points[r]
    a = l
    for i in range(l, r):
        print(points[i][0], points[i][1])
        if (points[i][0]**2 + points[i][1]**2) <= (pivot[0]**2 + pivot[1]**2):
            print("pre swap", points)
            points[a], points[i] = points[i], points[a]
            print("swap", points)
            a += 1
    points[a], points[r] = points[r], points[a]                
    return a
print(kClosest(points, k))