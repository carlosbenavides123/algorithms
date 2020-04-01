x = input()

def palin_int(x):
    if x < 0:
        return False
    res = 0
    num = x
    while num:
        res = res * 10 + num % 10
        num //= 10
    return res == x
print(palin_int(x))