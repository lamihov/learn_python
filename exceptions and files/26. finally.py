#finally. Используется когда необходимо чтобы код выполнялся независимо от того, возникают ошибки или нет
try:
    print("Hello")
    print(1 / 0)
except ZeroDivisionError:
    print("Divided by zero / Делится на ноль")
finally:
    print("This code will run no matter what / Этот код будет работать независимо от того, что")
#пример
try:
    print(1)
except:
    print(2)
finally:
    print(3)
#код в инструкции finally будет выоплняться даже при неперехваченном исключении
try:
    print(1)
    print (10 / 0)
except ZeroDivisionError:
    print(unknown_var)
finally:
    print("This is executed last / Это выполняется в последний раз")
#пример конструкции
try:
    print(1)
except:
    print(2)
finally:
    print(42)