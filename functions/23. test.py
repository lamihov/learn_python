#тест по функциям и модулям
def min(x,y):
  if x <= y:
    return x
  else:
    return y
#функция вычисляет сумму всех чисел от 0 до числа аргумента
def sum(x):
  res = 0
  for i in range(x):
    res += i
    return res
# самое большое число которое выведет программа = 0
def print_nums(x):
  for i in range(x): #вывод с 0 до 10
    print(i) 
    return
print_nums(10)
#Что выведет эта программа? 
def func(x):
  res = 0
  for i in range(x):
    res += i
  return res
print(func(4))