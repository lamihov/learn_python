#функции как объекты:
def multiply(x, y): #определяем функцию
  return x * y
a = 4
b = 7
operation = multiply #присваиваем переменной значение функции
print(operation(a, b))
#пример
def shout(word): 
  return word + "!"
speak = shout
output = speak("shout")
print(output)
#функции могут быть использованы как аргументы других функций
def add(x, y):
  return x + y
def do_twice(func, x, y):#func выполняет действие add (сложение)
  return func(func(x, y), func(x, y))# do_twice= (x + y) + (x + y)
a = 5
b = 10
print(do_twice(add, a, b))
#пример
def square(x):
  return x * x
def test(func, x):
  print(func(x))
test(square, 42)