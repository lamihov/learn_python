#функции списков. range - возвращает последовательность чисел начиная с 0 до 10
numbers = list(range(10))
print(numbers)
#пример .range
nums = list(range(5))
print(nums[4])
#при указании одного аргумента в range, выводит последовательность от 0; при указании двух аргументов - выводит диапазон от первого до второго [x1, x2)
numbers = list(range(3, 8))
print(numbers)
#пример
nums = list(range(5, 8))
print(len(nums))
#при указании трех аргументов, третий задает интервал числовой последовательности
numbers = list(range(5, 20, 2))
print(numbers)
#пример
nums = list(range(3, 15, 3))
print(nums[2])