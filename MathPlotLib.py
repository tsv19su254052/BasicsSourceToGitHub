# Interpreter 3.7


import matplotlib.pyplot
import numpy


"""
matplotlib - интерактивный режим в iPython
matplotlib notebook - интерактивные графики внутри Notebokk-а
matplotlib inline - статические изображения графиков внутри Notebook-а 
"""

plt = matplotlib.pyplot
"""
Стили:
 - classic,
 - fivethirtyeight,
 - seaborn-pastel,
 - seaborn-whitegrid (с серой сеткой),
 - ggplot,
 - grayscale,
 - dark_background (черный фон без сетки, тень легенды не видна)
"""
plt.style.use('classic')

# Верхний левый график
plt.subplot(2, 2, 1)
# Начало счета, конец счета, количество (по умолчанию 50)
x = numpy.linspace(0, 5, 1000)
# Рисуем линию, цикл выбор цветов по умолчанию - rgbcmyk (например, cyan, magenta, yellow)
plt.plot(x, numpy.sin(x), color='red', linestyle='--')
plt.title("Синус")
plt.xlabel('x, Радианы')
plt.ylabel('sin(x)')

# Верхний правый график
plt.subplot(2, 2, 2)
# Начало счета, конец счета, количество (по умолчанию 50)
x = numpy.linspace(0, 10, 1000)
# Рисуем линию
plt.plot(x, numpy.cos(x), color='green', linestyle='-.')
plt.title("Косинус")
plt.xlabel('x, Радианы')
plt.ylabel('cos(x)')

# Нижний левый график
plt.subplot(2, 2, 3)
# Начало счета, конец счета, количество (по умолчанию 50)
y = numpy.linspace(0, 5, 10000)
# Рисуем линию
plt.plot(y, numpy.tan(y), color='cyan', linestyle=':', label='график tan(x)')
# На самом деле пределы шкалы не фиксированы, график можно таскать мышка внутри его кадра
plt.xlim(-1, 6)  # Диапазон оси абсцисс - зазор 1 на сторону
plt.ylim(-50, 50)  # Диапазон оси ординат
plt.title('Тангенс')  # Название графика
plt.xlabel('x, Радианы')  # Обозначение оси абсцисс
plt.ylabel('tan(x)')  # Обозначение оси ординат
plt.legend(loc='upper right', frameon=True, fancybox=True, shadow=True)  # **если в plot упоминается label

# Выводим окошко с графиками (вызывать только один раз в конце скрипта)
plt.show()
