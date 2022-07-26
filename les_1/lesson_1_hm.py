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
Задание 2. Выполнить логические побитовые операции
'''

print(f'{bin(5) = }, {bin(6) = }')
print(f'{5 & 6 = }, {5 | 6 = }, {5 ^ 6 = }')
print( 5 << 2, 5 >> 2)

'''
Задание 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.
'''

def my_func_kx():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    k = (y1 - y2) / (x1 - x2)
    b = (y2 - k*x2)
    return(print(f'y = {k} * x + {b}'))

#my_func_kx()

'''
Задание 4. Написать программу, которая генерирует в указанных пользователем границах
'''

from random import randint, uniform, choice

print(randint(10,20))
print(uniform(0.5, 1.5))
print(choice([chr(i) for i in range(ord('e'), ord('z'))]))

'''
Задание 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
'''

print(f'First letter position {ord("c") - ord("a") + 1}, beetween letters {ord("z") - ord("k") - 1} letters')
print(f'Your letter is: {chr(5 + ord("a") - 1)}')