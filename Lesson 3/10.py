# -*- coding: utf-8 -*-

def xxx ():
    N = int(input("Введите количество чисел: "))
    K = int(input("Введите порядковый номер: "))
    fN = 0
    sN = 1
    sum = 0
    for i in range(2, N):
        c = sN
        sN = fN + sN
        fN = c
    if(i >= K - 1 ):
        sum += sN
    return sum
print(xxx())