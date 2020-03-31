_ = input()
input = [int(x) for x in input().split()]
hard = False
for i in range(len(input)):
    if input[i]:
        hard = True
        break
if hard:
    print("HARD")
else:
    print("EASY")