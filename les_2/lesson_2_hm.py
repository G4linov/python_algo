'''
Задание 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции вводятся пользователем. 
После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений. 
Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), 
то программа должна сообщать ему об ошибке и снова запрашивать знак операции. Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.
'''

while True:
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    sign = input('Введите знак операции: ')
    if ord(sign) > 48 or ord(sign) < 42:
        while ord(sign) > 47 or ord(sign) < 42:
            print('Вы ввели неверный знак')
            sign = input('Введите знак операции: ')
    if sign == '0':
        break
    elif sign == '+':
        print(f'Сумма: {a + b}')
    elif sign == '-':
        print(f'Разница: {a - b}')
    elif sign == '*':
        print(f'Произведение: {a * b}')
    elif sign == '/':
        print(f'Частное: {a / b}')


'''
Задание 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
'''

chet = 0
nechet = 0
user_input = input('Введите число: ')
for item in user_input:
    if int(item) % 2 == 0:
        chet += 1
    else:
        nechet += 1
print(chet, nechet)


'''
Задание 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.
'''

mas = []
user_input = input('Введите число: ')
for item in user_input:
    mas.append(item)
mas = list(reversed(mas))
print(''.join(mas))

'''
Задание 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
'''

n = int(input('введит кол-во эл:'))
i = 1
sum = 0

while n >= 0:
    if n % 2 == 0:
        sum += i*-1
        i = i/2
        n -= 1
    else:
        sum += i
        i = i/2
        n -=1
print(sum)

'''
Задание 5. Вывести на экран коды и символы таблицы ASCII, 
начиная с символа под номером 32 и заканчивая 127-м включительно. 
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
'''

n = 32

while n <= 127:
    mas = []
    i = 0
    while i < 10:
        mas.append(chr(n))
        i +=1
        n += 1
    print(' '.join(mas))

'''
Задание 6. В программе генерируется случайное целое число от 0 до 100. Пользователь 
должен его отгадать не более чем за 10 попыток. После каждой неудачной попытки должно
сообщаться больше или меньше введенное пользователем число, чем то,
что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.
'''

from random import randint

num = randint(0,100)
n = 0

while n < 10:
    n += 1
    user = int(input('Введите число: '))
    if user == num:
        print(f'Вы угадали. Число было: {num}')
        break
    elif user < num:
        print(f'Загаданное число больше. Осталось попыток: {10 - n}')
    elif user > num:
        print(f'Загаданное число меньше. Осталось попыток: {10 - n}')

if n == 10:
    print(f'Вы не угадали, число было: {num}')

'''
Задание 7. Напишите программу, доказывающую или проверяющую, 
что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.
'''

n = float(input('Введтие натуральное число '))
result = 0
resul1 = n*(n+1)/2

while n > 0:
    result += n
    n -= 1

print(result, resul1)