'''Рекурсия - функция, которая вызвает саму себя. Классический пример - вычисление факториала'''
x = int(input("Введите число:"))
def factorial(x):
    if x <= 1:
        return 1
    else:
        return x * factorial(x -1)
print(factorial(x))

'''Рекрсивные функции как и бесконечной циклы while, могут выполняться бесконечно.'''
'''Рекурсия может быть непрямой. Одна функция вызывает другую, затем вызывает первую, которая вызывает вторую и т.д.'''
def is_seven(x):
    if x == 0:
        return True
    else:
        return is_odd(x - 1)
def is_odd(x):
    return not is_seven(x)
print(is_odd(17))
print(is_seven(23))

#Пример
def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)
print(fib(4))