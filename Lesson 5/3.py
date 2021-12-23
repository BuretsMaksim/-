# -*- coding: utf-8 -*-

def xxx():
    i = 2
    a = 2
    b = 1
    N = int(input("Введите число - "))

    while a * i < N:
        a *= i
        b+=1
    print(a)
    print(b)
xxx()