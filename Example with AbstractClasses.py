# Interpreter 3.7 -> 3.11

from abc import ABC, abstractmethod


class MyValidator(ABC):
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.private_name, value)

    @staticmethod
    @abstractmethod
    def validate(value):
        pass


class Source(MyValidator):
    @staticmethod
    def validate(source):
        if isinstance(source, tuple):
            if all(isinstance(i, int) for i in source):
                return
            raise TypeError("ALl the items in \"source\" must be integers.")
        raise TypeError("\"source\" variable must be a tuple.")


class Target(MyValidator):
    @staticmethod
    def validate(target):
        if isinstance(target, tuple):
            if all(isinstance(i, int) for i in target):
                return
            raise TypeError("ALl the items in \"target\" must be integers.")
        raise TypeError("\"target\" variable must be a tuple.")


class MyClass:
    source = Source()
    target = Target()

    def __init__(self, source: tuple, target: tuple):
        self.source = source
        self.target = target
