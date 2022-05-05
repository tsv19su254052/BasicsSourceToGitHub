# Версия интерпретатора 3.6 (работает на 3.7)

'''
Объявление пользовательского класса и его методы
в отдельном файле с дальнейшим импортом, как внешнего пользовательского модуля
'''

__version__ = 1.2


class RootObjectClass():
    # инициализируем предка (Конструктор класса)
    def __init__(self, Name, Voice):
        self.name = Name
        self.voice = Voice

    def SelfCheck(self):
        print("Running... ")

    # метод предка
    def SayHello(self):
        print('Saying Hello ... ')
