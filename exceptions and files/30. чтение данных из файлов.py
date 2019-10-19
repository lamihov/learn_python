#содержимое файла открытого в режиме чтения можно получить с помошью метода read
file = open("filename.txt", "r") #открываем файл в режиме чтения
cont = file.read() #назначем переменную cont = содержимому файла
print(cont) #выводим на экран переменную cont
file.close #закрываем файл
#пример. 
file = open("test.txt") #открываем файл
cont = file.read() #назначем переменную cont = содержимому файла
print(cont) #выводим на экран переменную cont
file.close #закрываем файл
#чтобы прочесть только часть данных, в качестве аргумента функции read указывается определенное число байтов
file = open("filename.txt", "r")
print(file.read(16))
print(file.read(4))
print(file.read(4))
print(file.read())
file.close()
#сколько символов будет выведено в каждой строке, если символ равен одно байту
file = open("filename.txt", "r")
for i in range(21):
    print(file.read(4))
file.close()
#после того как содержимое файла было прочитано, дальнейшие вызовы метода чтения будут возвращать пустую строку
file = open("filename.txt", "r")
file.read()
print("Re-reading")
print(file.read())
print("Finished")
file.close
#пример
file = open("filename.txt", "r")
str = file.read()
print(len(str))
file.close
#чтобы получить каждую строку файла используется метод readlines, который возвращает список где каждый элемент является строкой
file = open("filename.txt", "r")
print(file.readlines())
file.close
#или
file = open("filename.txt", "r")
for line in file:
    print(line)
file.close