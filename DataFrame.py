# Interpreter 3.7


import pandas


# Простой пример DataFrame из трех списков
df_Example = pandas.DataFrame([[1, 2, 3, 4, 5],
                               [6, 7, 8, 9, 10],
                               [11, 12, 13, 14, 15]],
                              index=["a", "b", "c"],
                              columns=["aa", "bb", "cc", "dd", "ee"])
df_Example.index.name = "Rows"
print("\n DataFrame df_Example:")
print(df_Example)
# Транспонирование (меняем строки и столбцы местами
print("\n transposed DataFrame df_Example:")
print(df_Example.T)

# Пример DataFrame из списка двух частично перекрывающихся словарей
df_Dict = pandas.DataFrame([{'a': 1, 'b': 2},
                            {'b': 3, 'c': 4}])
# Этот промежуточный вывод нужен для примитивных сред, например, IDLE
print("\n DataFrame df_Dict:\n", df_Dict)
# print("\n transposed DataFrame df_Dict:\n", df_Dict.T)

# Объявляем исходный список
ListOne = []
# Длина списка
print("Введите длину строки DataFrame-а = ", end=" ")
# Ввод с клавиатуры (для надежности приводим к типу int)
Length = int(input())  # например, 25 столбцов
# Определяем исходный список
for count in range(Length):
    ListOne.append("cs_" + str(count))
# Вставляем в начало и сдвигаем остальное вправо
ListOne.insert(0, "Начало")
# Добавляем в конец
ListOne.append("Окончание")

# Делаем двухмерный список ListOne2 Каждая строка - список ListOne
# Высота нового списка
print("Введите количество строк DataFrame = ", end=" ")
# Ввод с клавиатуры (для надежности приводим к типу int)
Deepness = int(input())  # например, 45 строк
ListOne2 = [ListOne] * Deepness

# Делаем имена столбцов в цикле While и отдельной переменной-счетчика глобальной зоны видимости
ColumnNames = []
global g_count
g_count = 0
while g_count < len(ListOne):
    ColumnNames.append("c_" + str(g_count))
    g_count += 1

# Делаем имена строк
RowNames = []
g_count = 0
for count in range(Deepness):
    RowNames.append("s_" + str(count))

# Формируем DataFrame из ListOne2
df_ListOne2 = pandas.DataFrame(ListOne2,
                               index=RowNames,
                               columns=ColumnNames)
print(" DataFrame df_ListOne2:\n", df_ListOne2)

# Делаем список диапазоном с 1 до 120 с шагом 10
m = list(range(1, 120, 10))
print(m)
