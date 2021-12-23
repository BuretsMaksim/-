# -*- coding: utf-8 -*-

def xxx():
    a = 1
    b = 0
    while True:
        x = int(input("Введите число - "))
        if x == 0:
            break
        a+=1
        b += x
    print(b / a)
xxx()