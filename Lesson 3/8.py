# -*- coding: utf-8 -*-

def xxx():
    n = int(input('Введите число от 1 до 9: '))
    x = ''
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, sep='', end='')
        print()
    return 'End'
print(xxx())