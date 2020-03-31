num = int(input())
res = 0

while num > 0:
    if num >= 100:
        res += num // 100
        num = num % 100
    elif num >= 20:
        res += num // 20
        num = num % 20
    elif num >= 10:
        res += num // 10
        num = num % 10
    elif num >= 5:
        res += num // 5
        num = num % 5
    else:
        res += 1
        num -= 1
print(res)