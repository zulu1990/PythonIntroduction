class Student:
    def __init__(self, name, age, is_on_probation):
        self.__name = name
        self.__age = age
        self.__is_on_probation = is_on_probation

    def getName(self):
        return self.__name

