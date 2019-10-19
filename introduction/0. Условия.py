#Проверка на четность
x = int(input("Введите число: "))
if x % 2 == 0:
    print(x, " - четное число")
else:
    print(x, " - нечетное число")

#Несколько условий
print('''Кaкoй операционной системой вы пользуетесь?
1 - Windows 8
2 - Windows 7
3 - Windows Vista
4 - Windows ХР
5 - Windows 10''')
oss = (input("Введите число, соответствукщее ответу:"))
if oss == "1":
    print("Вы выбрали:Windows 8")
elif oss == "2":
    print("Вы выбрали:Windows 7")
elif oss == "3":
    print("Вы выбрали:Vista")
elif oss == "4":
    print("Вы выбрали: Windows ХР")
elif oss == "5":
    print("Вы выбрали: Windows 10")
elif not oss:
    print("ВЫ не ввели число")
else:
    print("Мы не смогли определить вашу операционную систему")