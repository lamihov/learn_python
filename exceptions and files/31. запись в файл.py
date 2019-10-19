#запись в файл. осуществляется методом write
file = open("newfile.txt", "w")
file.write("This has been written to file / Это было записано в файл")
file.close()
file = open("newfile.txt", "r")
print(file.read())
file.close()

#пример записи
file.write("Hello word")

#когда файл открывается в режиме записи все существуещее содержимое удаляется
file = open("newfile2.txt", "r")
print("Reading inital contents / Чтение начального содержания")
print(file.read())
print("Finished")
file.close()
file = open("newfile2.txt", "w")
file.write("Some new text / Какой-то новый текст")
file.close()
file = open ("newfile.txt", "r")
print("reading new contents / чтение нового содержания")
print(file.read())
print("Finished")
file.close()

#метод write в случае успеха возвращает количество байт, записанных в файле /// file.write(msg) == len(msg)
msg = "Hello world!"
file = open("newfile3.txt", "w")
amout_written = file.write(msg)
print(amout_written)
file.close