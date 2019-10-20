'''Магические методы - методи с двойным подчеркичанием (__init__). Часто применяются для переопределения операторов, таких операций как + и *'''
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)
print(result.y)
'''Распространные каналы:
__sub__ для (-)
__mul__ для (*)
__truediv__ для (/)
__floordiv__ для (//)
__mod__ для (%)
__pow__ для (**)
__and__ для (&)
__xor__ для (^)
__or__ для (|)
'''
class SpecialString:
    def __init__(self, cont):
        self.cont = cont
    def __truediv__(self,other):
        line = "=" * len(other.cont)
        return "/n".join([self.cont, line, other.cont])
spam = SpecialString("spam")
hello = SpecialString("hello world!")
print(spam / hello)
'''Магические методы для операций сравнения:
__it__ для (<)
__le__ для (<=)
__eq__ для (==)
__ne__ для (!=)
__gt__ для (>)
__ge__ для (>=)
'''
class SpecialString:
    def __init__(self, cont):
        self.cont = cont
    def __gt__(self, other):
        for index in range(len(other.cont)+ 1):
            result = other.cont[:index] + ">" + self.cont
            result += ">" + other.cont[index:]
            print(result)
spam = SpecialString("spam")
eggs = SpecialString("egss")
spam > eggs
'''Существует несколько магических методов, которые задают классам функциональность контейнеров
__len__ для len()
__getitem__ для индексации
__setitem__ для присваивания значения индексированному элементу
__delitem__ для удаления индексированного элемента
__iter__ для перебора объетов
__contains__ для in
'''
import random

class VagueList:
    def __init__(self,cont):
        self.cont = cont
    def __getitem__(self,index):
        return self.cont[index + random.randint(-1, 1)]
    def __len__(self):
        return random.randint(0, len(self.cont)*2)
vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])