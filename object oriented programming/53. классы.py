'''Класс оформляется с помощью ключевого слова class и всегда содержит методы класса(которые являются функциями)'''
class Cat: #определяем класс Cat
    def __init__(self, color, legs):
        self.color = color #атрибут цвет
        self.legs = legs #атрибут ноги
felix = Cat("ginger", 4) #объекты принадлежащие классу
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)
''' Метод __init__ - она вызывается когда создается объект класса, используется как функция. Все методы должны иметь self в кчестве первого параметра'''
class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs  = legs
felix =Cat("ginger", 4)
print(felix.color)

#пример
class Student:
    def __init__(self, name):
        self.name = name
test = Student("Bob")

''' Можно использовать другие методы, но перым доджен быть self.'''
class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def bark(self):
        print("Woof!")
fido = Dog("Fido", "brown")
print(fido.name)
fido.bark()

'''Классы могут также иметь атрибуты класса, которые создаются путем присвоения переменных в теле класса. На них можно ссылаться из экземпляров класса, либо из тела класса'''
class Dog:
    legs = 4
    def __init__(self, name, color):
        self.name = name
        self.color = color
fido = Dog("Fido", "brown")
print(fido.legs)
print(Dog.legs)

#пример
class Student:
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print("Hi from" + self.name)
s1 = Student("Amy")
s1.sayHi()

'''Попытка вызова атрибута экземпляра, который не был определен, вызывает ошибку AttributeError'''
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
react = Rectangle(7,8)
print(Rectangle.color)