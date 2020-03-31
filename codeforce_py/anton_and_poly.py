
hmap = {"Tetrahedron": 4, "Cube": 6, "Octahedron": 8, "Dodecahedron": 12, "Icosahedron": 20}

num = int(input())
res = 0
for i in range(num):
    res += hmap[input()]
print(res)