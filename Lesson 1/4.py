# -*- coding: utf-8 -*-

print("Введите количество секунд")
seconds = int(input())
day = seconds % 86400
hour = seconds // 3600
min = seconds // 60
sec = seconds % 60
print(day, ":", hour, ":", min, ":", sec)