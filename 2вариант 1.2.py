from math import tan
from math import pi
from itertools import count


def plosh(S,n1):
    area = (n1 * (S ** 2)) // (4 * tan(pi / n1))
    print(area)


def Summ(n2):
     print((n2 * (n2 * 1) // 2))


while 1 > 0:
    txt = input('Введите номер задание')
    if txt == '1':
        S = int(input('Введите значение длины стороны:'))
        n1 = int(input('Введите количество сторон:'))
        plosh(S,n1)
    elif txt == '2':
        n2 = int(input('Введите количество цифр'))
        Summ(n2)
        
