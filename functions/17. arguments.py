#аргументы
def print_with_exclamation(word):
  print(word + "!")
print_with_exclamation("spam")
print_with_exclamation("eggs")
print_with_exclamation("python")
#пример
def print_double(x):
  print(2*x)
print_double(3)
#функции с более чем одни аргументом указываются через запятую
def print_sum_twice(x, y):
  print(x + y)
  print(x * y)
print_sum_twice(5, 8)
#пример: определить функцию которая принимает два аргумента, перемножает и выводит результат
def print_mult(x, y):
  print(x * y)
print_mult(4, 5)
#аргументы функций могут быть использованы в качестве переменных, но на них нельзя ссылаться извне
def function(variable):
  variable += 1
  print(variable)
function(7)
print (variable) #выдаст ошибку: NameError
#определить функцию, которая выведет Yes если параметр - четные, иначе No
def even(x):
  if x%2 == 0:
    print("Yes")
  else:
    print("No")
even(7)