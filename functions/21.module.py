''' модули. схема использования: добавить import module_name в верхнюю часть, а затем с помощью module_name.var вызвать функции и значения с именем var'''
import random
for i in range(5):
  value = random.randint(1, 6)
  print(value)
#пример
import math
num = 10
print(math.sqrt(num))
'''существует еще один способо импортирования, когда нужно получить только определенные переменные. Синтаксис имеет форму from module_name import var, и var можно использовать как обычную переменную'''
from math import pi
print(pi)
#пример
from math import sqrt, cos
#можно импортировать модуль под другим именем используя ключевое слово as
from math import sqrt as square_root
print(square_root(100))