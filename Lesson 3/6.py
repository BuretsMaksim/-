# -*- coding: utf-8 -*-

def xxx():
    pr = 1
    n = int(input('Введите натуральное число: '))
    for i in range(1, n + 1):
        pr *= i
    print(pr)
    return 'End'
print(xxx())