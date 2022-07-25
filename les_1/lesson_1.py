'''
Задание 1. Сравниваем числа и находим максимум
'''

def my_max_2(a,b):
    max_int = a
    if b > max_int:
        max_int = b
    return(max_int)

def my_max_3(a,b,c):
    max_int = a
    if b > max_int:
        max_int = b
    if c > max_int:
        max_int = c
    return(max_int)


#a, b, c = input().split()
#a, b, c = map(int, [a,b,c])
#print(my_max_3(a,b,c))

'''
Задание 2. Вычислить значение функции y=f(x)
'''

def my_func(x):
    if x > 3:
        print(2 * x + 5)
    elif x > -3:
        print(abs(x))
    else:
        print(0)

#x = int(input())
#my_func(x)

'''
Задание 3. Проверить делимость одного числа на другое.
'''

def test_div(a,b):
    if a % b == 0:
        print(f'{a} divs {b}, result {a // b}')
    else:
        print(f'{a} not div {b}')
        

#a, b = map(int, input().split())
#test_div(a,b)

'''
Задание 4. Перевести байты в килобайты или наоборот
'''

def byte(a):
    return(a * 1024) 

def kilobyte(a):
    return(a // 1024)

a = int(input('Write number: '))
key = input('k - to kilobyte, b - to byte: ')

if key == 'b':
    print(byte(a), 'byte')
elif key == 'k':
    print(kilobyte(a), 'kilobyte')
else:
    print('Error')