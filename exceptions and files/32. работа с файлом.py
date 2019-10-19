#работа с файлами. рекомендуется всегда закрывать файл после работы с ними
try:
    f = open("filename.txt")
    print(f.read())
finally:
    f.close()

#пример
try:
    f = open("filename.txt")
    print(f.read())
    print(1 / 0)
finally:
    f.close()

#еще один способ сделать это с помощью инструкции with - создается временная переменная f
with open("filename.txt") as f:
    print(f.read())

#пример
with open("test.txt") as f:
    print(f.read())