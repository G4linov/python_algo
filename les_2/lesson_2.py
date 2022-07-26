# Factorial
#

def factorial_1(n):
    if n <= 0:
        return 1
    else:
        return n * factorial_1(n-1)

def factorial_2(n):
    item = 1
    for i in range(1, n+1):
        item *= i
    return item

def factorial_3(n):
    item = 1
    i = 1
    while i <= n:
        item *= i
        i += 1
    else:
        print(f'{i = }')
    return item

def factorial_4(n):
    item = 1
    i = 1
    while True:
        i += 1
        item *= i
        if i == n:
            break
    else:
        print(i)
    return item

print(factorial_1(10))
print(factorial_2(10))
print(factorial_3(10))
print(factorial_4(10))

