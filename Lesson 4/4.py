# -*- coding: utf-8 -*-

def xxx():
    c = input()
    first = c[:c.find(' ')]
    second = c[c.find(' ') + 1:]
    print(second+' '+first)
    return "Конец"
print(xxx())