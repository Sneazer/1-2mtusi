from math import tan
from math import pi
from time import time, sleep
from itertools import count
from threading import *
from datetime import datetime


now = datetime.now()

current_time = now.strftime("%M")




def ploshForcircl(S,n1):
    time1 = time()
    area = (n1 * (S ** 2)) // (4 * tan(pi / n1))
    print(area)

def TimePlosh(S,n1):
    time1 = time()
    area = (n1 * (S ** 2)) // (4 * tan(pi / n1))
    return (time1, 'функция отвечает за время нахождения площади')

def TiemSumm(n2):
    time1 = time()
    summ = (n2 * (n2 + 1) // 2)
    return (time1, 'Функция отвечает за время нахождения суммы')

def Plosh(S,n1):
    time1 = time()
    area = (n1 * (S ** 2)) // (4 * tan(pi / n1))
    return (area,'функция отвечает за площадь')

def Summ(n2):
    time1 = time()
    summ = (n2 * (n2 + 1) // 2)
    return (summ, 'Функция отвечает за сумму цифр')


def SummForcircl(n2):
    time1 = time()
    summ = (n2 * (n2 + 1) // 2)
    print(summ)
txt1 = input('Выберете слудующее действие (1)Декоратор, 2)Цикл):')

if txt1 == '1' or txt1 == 'Декоратор':
    print('Пишите функцию:')
elif txt1 == '2' or txt1 == 'Цикл':
    while 1 > 0:
        txt = input('Введите номер задания на которое хотите увидеть ответ(1; 2; 3)1 и 2 одновременно;4) 1 и 2 поочередно; 5)конец): ')
        if txt == '1':

            S = int(input('Введите значение длины стороны: '))
            n1 = int(input('Введите количество сторон: '))

            ploshForcircl(S, n1)

            time2 = time()

            print(f"Время затраченное на первое задание: {'%s seconds' %time2}")

        elif txt == '2':
            n2 = int(input('Введите количество цифр, которые хотите сложить: '))

            SummForcircl(n2)

            time2 = time()

            print(f"Время затраченное на первое задание: {'%s seconds' %time2}")


        elif txt == '3' or txt == '1 и 2 одновременно':
            S = int(input('Введите значение длины стороны: '))
            n1 = int(input('Введите количество сторон: '))
            n2 = int(input('Введите количество цифр, которые хотите сложить: '))

            t1 = Thread(target=ploshForcircl, args=(S, n1,))
            t2 = Thread(target=SummForcircl, args=(n2,))

            time1  = time()

            t1.start()
            t2.start()

            t1.join()
            t2.join()

            time2 = time()

            print(f"Время выполнения двух заданий одновременно: {'%s seconds' %time2}")


        elif txt == '4':
            S = int(input('Введите значение длины стороны: '))
            n1 = int(input('Введите количество сторон: '))
            n2 = int(input('Введите количество цифр, которые хотите сложить: '))

            SummForcircl(n2)
            time1 = time()
            ploshForcircl(S, n1)

            time2 = time()

            timeDelt = time1 + time2

            print(f"Время выполнения двух заданий одновременно: {'%s seconds' %timeDelt}")


        elif txt == 'конец' or txt == 'Конец' or txt == '5':
            print('До свидания!')
            break
