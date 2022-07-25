'''
Необходимо понять в каком классе материал
'''

a = float(input('Write number: '))

lv = 60.3
uv = 61.3

classif = int(a // lv + a // uv)
print(classif)

if a > uv:
    print(2)
elif a > lv:
    print(1)
else:
    print(0)