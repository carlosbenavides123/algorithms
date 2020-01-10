def tower(n):
    def place(n, from_peg, to_peg, use_peg):
        print(n, from_peg, to_peg, use_peg)
        if n > 0:
            place(n-1, from_peg, use_peg, to_peg)
            operations.append([from_peg, to_peg])
            place(n-1, use_peg, to_peg, from_peg)
    operations = []
    place(n, 0, 1, 2)
    return operations


print(tower(3))
