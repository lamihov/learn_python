#какое число не вернет эта программа? // 2
try:
    print(1)
    print(20/0)
    print(2)
except ZeroDivisionError:
    print(3)
finally:
    print(4)
#открыть файл в двоичном режиме записи
open("test.txt", "wb")
#открыть и прочитать файл, вывести сообщение об ошибке в случае исключения
try:
    with open("test.txt") as f:
        print(f.read())
except:
    print("Error")
#каким будет самое большое число, которое вернет эта программа? // 3
try:
    print(1)
    assert 2 + 2 == 5
except AssertionError:
    print(3)
except:
    print(4)