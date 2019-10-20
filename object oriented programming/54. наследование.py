''' При наследовании могут существовть как уникальные методы для каждого класса, так и общие, которые наследуются от суперкласса'''
class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
class Cat(Animal):
    def purr(self):
        print("Purr")
class Dog(Animal):
    def bark(self):
        print("Woof")
fido = Dog("Fido","brown")
print(fido.color)
fido.bark()

''' Класс наследующий атрибуты или методы другого класса, называется подклассом. Класс из которого происходит наследования называется суперклассом. 
Если подкласс имеет такие же методы/атрибуты, что и суперкласс, то он их переопределяет'''
class Wolf:
    def __init__(self,name, color):
        self.name = name
        self.color = color
    def bark(self):
        print("Grrr")
class Dog(Wolf):
    def bark(self):
        print("Woof")
husky = Dog("Max","grey")
husky.bark()

#пример
class A:
    def method(self):
        print(1)
class B:
    def method(self):
        print(2)
B().method()
'''Наследование может быть непрямым, один класс может наследовать атрибуты от второго, второй может наследовать атрибуты от третьего'''
class A:
    def method(self):
        print("A method")
class B(A):
    def another_method(self):
        print("B method")
class C(B):
    def third_method(self):
        print("C method")
c = C()
c.method()
c.another_method()
c.third_method()

#пример
class A:
    def a(self):
        print(1)
class B(A):
    def a(self):
        print(2)
class C(B):
    def c(self):
        print(3)
c =C()
c.a()

'''Функция super - указывает на родительский класс, предназначена для поиска метода по его имени в суперклассе'''
class A:
    def spam(self):
        print(1)
class B(A):
    def spam(self):
        print(2)
        super().spam()
B().spam()