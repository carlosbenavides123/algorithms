num = input()
num = int(num)

hate = "I hate it"
love = "I love it"

res = "I hate it"

for i in range(1, num):
    phrase = ""
    if i % 2 == 1:
        phrase = love
    else:
        phrase = hate
    res = res[:-2] + "that " + phrase
print(res)
