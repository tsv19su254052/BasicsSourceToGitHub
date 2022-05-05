# -*- coding: utf-8 -*-
# Версия интерпретатора 3.6 (работает на 3.7)

import itertools
import os
import sys
import platform
#import cpuinfo # такой библиотеки не найдено

Source = 'aad', 'aae', 'aad', 'aad', 'fgh', 'aad', 'fgh', 1, 8, 12, 'rfg', '554', 2, 'Aae'
print(Source)
# Убираем повторы без сохранения того же порядка
OutPut = set(Source)
print(OutPut)
# Убираем только повторы, идущие подряд, но с сохранением исходного порядка
OutPutNew = [el for el, _ in itertools.groupby(Source)]
print(OutPutNew)

String = " This is a Test String... \n"
String += " TestLine 1 \n"
String += " TestLine 2 \n"
try:
    OutPutFile = open("LogReportTest" + ".txt", 'a')
    OutPutFile.write(String)
    OutPutFile.write("\n")
    OutPutFile.write((str(OutPut)))
    OutPutFile.write("\n\n")
except IOError:
    print(" Ошибка дозаписи в LogReport")
finally:
    OutPutFile.close()

print(String)

os.rename("DataSQL33.json", "DataSQL.json")

#cpuinfo.cpu.info()
