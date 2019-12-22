def fib(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fib(num - 2) + fib(num - 1)


print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))

print("-----------------")


def fib(num):
    if num == 0:
        return 0
    if num == 1:
        return 1

    mem = [0] * num
    mem[0] = 1
    mem[1] = 1
    for i in range(2, num):
        mem[i] = mem[i-1] + mem[i-2]
    print(mem)
    return mem[-1]


print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))


def fib(num):
    if num == 0:
        return 0
    if num == 1 or num == 2:
        return 1

    l = r = 1
    fib = l + r

    for i in range(2, num):
        fib = l + r
        l = r
        r = fib
    return fib


print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
# 1 1 2 3 5
