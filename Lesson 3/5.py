# -*- coding: utf-8 -*-

def xxx ():
    sum = 0
    n = int(input('Введите натуральное число: '))
    for i in range(1, n + 1):
        sum += i**3
    print(sum)
    return 'End'
print(xxx())