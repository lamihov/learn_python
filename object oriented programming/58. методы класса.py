'''
Методы объектов, рассмотренные ранее, вызываются экземпляром класса, который затем передается в параметр метода self.
Методы класса несколько другие: они вызываются классом, который передается параметру cls метода.
Чаще всего это используется в фабричных методах: создается экземпляр класса, при этом используются иные параметры, чем те, которые обычно передаются в конструктор класса.
Методы класса оформляются с декоратором classmethod.
'''
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height
    @classmethod #метод класса
    def new_square(cls, side_length):
        return cls(side_length, side_length)

square = Rectangle.new_square(5)
print(square.calculate_area())

#new_square - метод класса и вызывается для класса, а не для экземпляра класса. Он возвращает новый объект класса cls.
class Person:
    def __init__(self, name):
        self.name = name
    @classmethod #метод класса
    def sayHi(cls):
        print("Hi")

'''
Статические методы похожи на методы класса с тем отличием, что они не берут никаких дополнительных аргументов;
 они аналогичны обычным функциям класса. Они оформляются с декоратором staticmethod.
Статические методы ведут себя как обычные функции с тем отличием, что вы можете вызывать их экземпляром класса.
'''

class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

@staticmethod #статистический метод класса
def validate_topping(topping):
    if topping == "pineapple":
        raise ValueError("No pineapples!")
    else:
        return True

ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)