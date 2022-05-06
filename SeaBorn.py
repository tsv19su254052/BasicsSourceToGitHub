# Interpreter 3.7


import seaborn
import matplotlib
import numpy


# Есть интеграция с DataFrame из Pandas - моя правка 02
seaborn.set()
# Задаем диапазон и число точек вычисления
x = numpy.linspace(0, 15, 10000000)  # больше 10000000 не делать

# Считаем облако точек
y = numpy.sin(x)
#y = numpy.cos(x)
print(" x = ", x, "\n y = ", y)

# Выводим облако точек
plt = matplotlib.pyplot
plt.plot(x, y)
plt.legend('ABCD', ncol=2, loc='upper right', shadow=True)
plt.show()
