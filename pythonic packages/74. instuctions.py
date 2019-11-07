'''
Инструкция else наиболее часто используется вместе с инструкцией if, но также может следовать за циклами for или while, что придает ей иное значение.
В этом использовании код в ней вызывается, если цикл завершается нормально (когда инструкция break не останавливает цикл).
'''

for i in range(10):
    if i == 999:
        break
else:
    print("Unbroken 1")

for i in range(10):
    if i == 5:
        break
else:
    print("Unbroken 2")

#пример
for i in range(10):
    if i > 5:
        print(i)
        break
    else:
        print("7")

'''Инструкцию else также можно использовать с инструкциями try/except.
В этом случае код внутри них выполняется только, если ошибок не происходит в инструкции try.
'''
try:
    print(1)
except ZeroDivisionError:
    print(2)
else:
    print(3)

try:
    print(1/0)
except ZeroDivisionError:
    print(4)
else:
    print(5)

#пример (4)
try:
    print(1)
    print(1 + "1" == 2)
    print(2)
except TypeError:
    print(3)
else:
    print(4)