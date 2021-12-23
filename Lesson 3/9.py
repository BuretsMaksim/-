# -*- coding: utf-8 -*-

def xxx ():
    n = int(input('Введите количество чисел: '))
    x = 0
    y = 1
    sum = 1
    for i in range(2, n):
        a = y
        y = x + y
        x = a
        sum += y
    print("Сумма равна ", sum)
    return 'End'
print(xxx())