# -*- coding: utf-8 -*-

def xxx():
    s = 0
    n = int(input('Введите количество чисел: '))
    for i in range(n):
        s += int(input('Введите эти числа:'))
    print(s)
    return 'End'
print(xxx())