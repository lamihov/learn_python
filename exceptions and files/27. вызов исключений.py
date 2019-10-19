#вызов исключений. Вызов исключений происходит с помощью инструкции raise
print(1)
raise ValueError
print(2)
#пример
try:
    print(1 / 0)
except ZeroDivisionError:
    raise ValueError
#исключение можно вызвать с указанием аргумента который представляет ее описание
name = "123"
raise NameError("Invalid name!")
#пример
num = input(":")
if float(num) < 0: #если введенное число меньше 0, то вызваем ошибку
    raise ValueError("Nagative")
#В блоках except инструкция raise может использоваться без аргументов, будет вызвано предыдущее исключение
try:
    num = 5 / 0
except:
    print("An error occured / Произошла ошибка")
    raise