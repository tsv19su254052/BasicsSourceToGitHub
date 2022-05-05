# Импорт только одного класса из пользовательской библиотеки
# (имя файла типа *.py в этой же папке - еще одного скрипта на Python-е)
# Компилируется и кладется в папку "__pycache__"

# Импорт пользовательской библиотеки (файла в этой же папке)
# from Class_RootObjectClass import RootObjectClass
import Class_RootObjectClass
import AbstractClass_RootObjectAbstractClass

# Интерфэйсы, декораторы, метаклассы ...

# Сделать наследника без расширения функционала и сразу дать параметры на вход конструктору
o = Class_RootObjectClass.RootObjectClass("Hunter Jake", True)
a = AbstractClass_RootObjectAbstractClass.RootObjectAbstractClass("Shannon and Patrice", False)
# Наследник должен работать только следующим образом:
# - брать параметры на вход,
# - присваивать их своим внутренним переменным,
# - работать с ними,
# - выдать результат на выход
o.SayHello()
o.SelfCheck()
a.SayHi()
a.SelfCheck()
print(" Текущая версия предка = ", Class_RootObjectClass.__version__)
print(" Имя предка = ", Class_RootObjectClass.RootObjectClass.__name__)
print(" Имя наследника = ", o.name)
if o.voice:
    print(" у класса-наследника есть свой голос")
else:
    print(" у класса-наследника нет своего голоса")
