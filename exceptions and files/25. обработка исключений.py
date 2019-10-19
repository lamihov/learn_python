''' обработка исключений. Чтобы обойти исключение и выполнить код можно использовать конструкцию try/except. 
Блок try  - содержит код под сомнением, который может вызвать исключение. В случае исключения выполнение кода в блоке try прерывается 
и передается коду в блок except. Если не происходит никакой ошибки, код в блоке except не выполняется'''
try:
    num1 = 7
    num2 = 0
    print(num1 / num2)
    print("Done calculation")
except ZeroDivisionError:
    print("An error occured")
    print("due to zero division")
#пример
try:
    variable = 10
    print (10 / 2)
except ZeroDivisionError:
    print("Error")
print("Finished")
''' инструкция try может иметь несколько блоков except (указываются в круглых скобках), для различных исключений'''
try:
    variable = 10
    print(variable + "hello")
    print (variable / 2)
except ZeroDivisionError:
    print("Divided by zero")
except (ValueError, TypeError):
    print("Error occured")
#пример
try:
    meaning = 42
    print(meaning / 0)
    print("the meaning of life")
except(ValueError, TypeError):
    print("ValueError or TypeError occurred")
except ZeroDivisionError:
    print("Divided by zero")
''' Выражение except не имеющее определенных исключений будет перехватывать все ошибки'''
try:
    word = "spam"
    print(word / 0)
except:
    print("An error occurred")
#пример
try:
    num1 = input(":")
    num2 = input(":")
    print(float(num1)/float(num2))
except:
    print("invalid input")