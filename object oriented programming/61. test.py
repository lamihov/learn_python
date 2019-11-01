#Сделать атрибут egg строго частным, и сослаться на него вне класса
class Test:
    __egg = 7

t = Test()
print(t._Test__egg)

#Создать setter для свойства name
class Person:
    def __init__(self, name):
        self._name = name

@property
def name(self):
    return self._name

@name.setter
def name(self, value):
    self._name = value