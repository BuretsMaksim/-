# -*- coding: utf-8 -*-

def xxx ():
    print("Введите 3 случайных числа")
    q = int(input())
    w = int(input())
    e = int(input())
    if q == w and q == e and w == e:
        return "3"
    else:
        pass
    if q == w or q == e or w == e:
        return "2"
    else:
        return "1"
print(xxx())