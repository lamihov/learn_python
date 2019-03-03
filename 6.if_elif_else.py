#простой цикл if - else
salary = 50000
if salary == 60000:
    print("good")
else:
    print("bad")

#вложенный цикл
num = 7
if num == 5:
    print("номер равен 5")
else:
    if num == 11:
        print("номер равен 11")
    else:
        if num == 7:
            print ("номер равен 7")
        else:
            print ("номер не равен 5, 7, 11")

#инструция elif - более короткий способ создания цепочек else / if
num = 7
if num == 5:
    print("номер равен 5")
elif num == 11:
    print ("номер равен 11")
elif num == 7:
    print ("номер равен 7")
else:
    print ("номер не равен 5, 7, 11")