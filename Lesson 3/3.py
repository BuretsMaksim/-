# -*- coding: utf-8 -*-

def xxx ():
    a = int(input('Введите первое большее число: '))
    b = int(input('Введите второе меньшее число: '))
    for i in range(a, b - 1, -1):
        if i % 2 !=0:
            print(i)
    return "Конец"
print(xxx())