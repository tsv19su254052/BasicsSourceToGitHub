# Версия интерпретатора 3.6 (работает на 3.7)


# Объявление пользовательского метакласса и его методы
# в отдельном файле с дальнейшим импортом, как внешнего пользовательского модуля

import abc

__version__ = 0.2

# Абстрактный метакласс - только для наследования
class RootObjectAbstractClass():
    # инициализируем предка (Конструктор класса)
    def __init__(self, Name, Voice):
        self.Name = 'AbstractName'
        self.Voice = 'AbstarctVoice'

    # методы предка
    def SelfCheck(selfself):
        print("Running...")

    def SayHi(self):
        print("Saying Hi ...")

