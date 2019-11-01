'''В свойствах можно настроить доступ к атрибутам экземпляра.
Чтобы создать свойства, непосредственно перед методом помещается декоратор property:
при вызове атрибута экземпляра с таким же именем, что и у метода, вместо него будет вызван метод.
Один из распространенных способов их применения - присвоение атрибуту свойства «только для чтения».
'''

class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

@property
def pineapple_allowed(self):
    return False

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True

#создание свойства isAdult
class Person:
    def __init__(self, age):
        self.age = int(age)

@property
def isAdult(self):
    if self.age > 18:
        return True
    else:
        return False

'''
Свойства также могут быть заданы с помощью функций setter/getter.
- Функция setter устанавливает значение соответствующего свойства.
- Функция getter возвращает значение.
Чтобы определить setter, используется декоратор с таким же именем, что и у свойства, с последующим ключевым словом setter, разделенные точкой.
Точно так же определяются функции getter.
'''
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        self._pineapple_allowed = False

@property
def pineapple_allowed(self):
    return self._pineapple_allowed

@pineapple_allowed.setter
def pineapple_allowed(self, value):
    if value:
        password = input("Enter the password: ")
        if password == "Sw0rdf1sh!":
            self._pineapple_allowed = value
else:
    raise ValueError("Alert! Intruder!")

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)