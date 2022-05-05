"""
Created on Sat Mar 24 19:29:10 2018

Базовые (комплектные с Python) типы:
    неизменяемые:
        - None,
        - числа (целые, вещественные, комплексные, рациональные, фиксированной точности),
        - кортежи,
        - строки,
        - множества,
    изменяемые:
        - логические,
        - списки,
        - словари - Отображение, хэш-таблица,
        - файлы,
(см. прилагаемую структуру типов в Python)
Последовательности:
    - строки,
    - списки,
    - кортежи.

@author: Sergey
"""


# Главное Примечание:
# Любой тип данных - это класс
# Выяснение типа данных по ходу работы скрипта не имеет смысла, так как
# Python имеет динамическую типизацию

import math
import decimal
import os


# Числа
bool1 = True  # логическое
bool2 = False
a = 5  # Целое
b = 10.5  # Вещественное
e_nan = float('nan')  # неопределенное вещественное
infinity1 = float('inf')  # бесконечно большое вещественное
infinity2 = float('inf')
negative_infinity = float('-inf')  # минус бесконечность
k = None  # выражения с None не работают -> ошибка, в условиях не False и не True
x = complex(a, b)  # Комплексное число
b += 2
b *= 5
b /= 1.5
f = a / b
h = b ** a
g = 0x118  # целое в 16-чной форме
q = 1.87e50

res1 = infinity1 - infinity2  # бесконечность - бесконечность = неопределенное число
res2 = infinity1 + negative_infinity  # бесконечность + минус бесконечность = неопределенное число

if not k and a == 5:
    print(" a=", str(a), " k=", str(k))

if e_nan:
    print(" e=", str(e_nan))


j = math.pow(3, 4)
# j = 3 ** 4 - 81
y = math.log(5, 10)
ee_nan = math.nan  # с помощью библиотеки math
if math.isnan(ee_nan):
    print(" ee_nan =", str(ee_nan))

e_NaN = decimal.Decimal('nan')

# nan не равно nan и не равно NaN
if e_nan == ee_nan:
    print(" e -> ee_nan")
if ee_nan == e_NaN:
    print(" ee_nan -> e_NaN")
if e_nan == e_NaN:
    print(" e -> e_NaN")


# Последовательности (кортежи, списки, словари)

# Кортеж - теоретически как бы неизменяемый, короче и быстрее
# c = tuple(('naa', 'maa', 'paa'))
c = ('na', 'ma', 'pa')
c += ('qaa', 6, 1.4, 'Окончание кортежа')
dir(c)
# help(c.__new__)  # вывод справки по этому методу в командную строку
print('c = ', c)
# print(type(c))  # Это class?

# Список - изменяемый
# d = list((1, 2, 3, 4, 5))
d = [1, 2, 3, 4, 5, 6]
d[1] = 3;
d *= 2
d.append(6);
d.insert(0, 'Начало списка')  # несколько команд в одну строку
d.append('Окончание списка')
d.remove(5)  # удаление по содержимому
d.insert(2, 2)
d.insert(4, 'в Серединке списка')
d.remove(6)
d += [0 for i in range(10)]

# Убираем нули с конца списка
for i in reversed(range(len(d))):
    if d[i] == 0:
        d.pop(i)
    else:
        break

# del d[2] # удаление по номеру - выдает ошибки
print('d = ', d)

dex = ['nan', 'nbn', 'ncn', 'ndn', 'nen', 0, 'nan', 'nan', 1, 'nkn', 'nfn']
dexS = set(dex)
dexSstr = sorted(dexS, key=lambda x: isinstance(x, str))
dexSint = sorted(dexS, key=lambda x: isinstance(x, int))

dex2 = ['nan' for i in range(20)]
dex2S = set(dex2)


# Вложенный список (двухмерный массив - матрица)
# dd = list(((1., 2., 3.,), (4., 5., 6.), (7., 8., 9.)))
dd = [[1., 2., 3.], [4., 5., 6.], [7., 8., 9.]]
print(" dd = ")
print(dd)

# Размерность та же, умножаем количество строк в 5 раз, строки заполняем содержимым dd
# Размерность остается та же
dd2 = 5 * dd
print('dd2 = ')
print(dd2)

# Словарь - изменяемый, хэш-таблица
# m = dict(Ivan='Palich', Vasiliy='Valeriy')
m = {'Ivan':'Palich', 'Vasiliy':'Valeriy'}
m['Vanya'] = 'Vasilev'
print(m.get('Vanya'))
print(m.get("Empty"))

# Строка
st = 'MainName'
st += '_5_'  # конкатенация, применение полиморфизма
print(st)
print("Имя главного модуля скрипта = ", str(__name__))

# Срез списка
d1 = d[2:4]
d2 =d[2:6:2]
# С помощью функции
d3 = d[slice(2, 6, None)]
d4 = d[slice(2, None, 2)]

# Выводим имя пользователя Windows
UN = os.getlogin()
print("Имя пользователя Windows = ", str(UN))
