'''Модуль itertools - стандартная библиотека, которая содержит различные функции:
- count - бесконечная прогрессия вверх от заданного числа;
- cycle - бесконечный перебор итерируруемого объекта;
- repeat - повтор объекта бесконечное число раз'''
from itertools import count
for i in count(3):
    print(i)
    if i >= 11:
        break

'''
- takewhile - возвращает элементы, которые удовлетворяют предиктивной функции;
- chain - объединяет несколько итерируемых объектов в один;
- accumulate - возвращает сумму значений внутри итерируемого объекта;'''
from itertools import accumulate, takewhile
nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x: x < 6, nums)))

#пример
from itertools import takewhile
nums = [2, 4, 6, 7, 9, 8]
a = takewhile(lambda x: x%2 == 0, nums)
print(list(a))

'''Наличие комбинаторных функций product и permulation - перебор всех возможных комбинаций'''
from itertools import product, permutations
letters = ("A", "B", "C", "D")
print(list(product(letters, range(2))))
print(list(permutations(letters)))

#пример
a = {1,2}
print(len(list(product(range(3), a))))