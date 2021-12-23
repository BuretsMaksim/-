# -*- coding: utf-8 -*-

def xxx ():
    pr = 1
    sum = 0
    n = int(input('Введите натуральное число: '))
    for i in range(1, n + 1):
        pr *=  i
        sum += pr
    print(sum)
    return 'End'
print(xxx())