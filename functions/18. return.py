#возвраст из функции. int и str - возвращают значение для дальнейшего использования, с помощью инструкции return
def max(x, y):
  if x >= y:
    return x
  else:
    return y
print (max(4, 7))
z = max(8,5)
print(z)
#определить функцию, которая сравнивает длину аргументов и возвращает самый короткий
def shorter_string(x, y):
  if len(x) <= len(y):
    return x
  else:
    return y
#после того, как функция вернула значение, она больше не выполняется
def add_numbers (x, y):
  total = x + y
  return total
  print("This won't be printed")#не выполняется
print(add_numbers(4, 5))
#пример
def print_numbers():
  print(1)
  print(2)
  return
  print(4)
  print(6)
print(print_numbers)