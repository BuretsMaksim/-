# -*- coding: utf-8 -*-

def xxx():
    stroka = input("Введите строку - ")
    symbol = input("Введите символ для удаления - ")
    print(stroka.replace(symbol, ""))
    return "Конец"
print(xxx())