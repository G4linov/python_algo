'''
Задание 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
'''

def My_result(x):
    sum = 0
    multiply = 1
    while x > 0:
        sum += x % 10
        multiply *= x % 10
        x = x // 10
        #print(x, sum, multiply)
    return(sum, multiply)

#x = int(input('Write number: '))
#print(My_result(x))

'''
Задание 2. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.
'''

def my_func_kx():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    k = (y1 - y2) / (x1 - x2)
    b = (y2 - k*x2)
    return(print(f'y = {k}x + {b}'))

#my_func_kx()