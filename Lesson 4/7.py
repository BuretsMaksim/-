# -*- coding: utf-8 -*-

def xxx():
    c=input()
    print(c[:c.find('h')] + c[c.rfind('h') + 1:])
    return "Конец"
print(xxx())