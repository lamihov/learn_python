#выводит значение i, пока i не будет равен 5. while (до тех пор пока)
i = 1
while i <= 5:
    print(i)
    i = i + 1
print("Finshed")
#бесконечный цикл
while 1 == 1:
    print ("in the loop - в петле")
#использования инструкции break (стоп)
i = 0
while 1 == 1:
    print(i)
    i = i + 1
    if i >= 5:
        print ("Breking")
        break
print("Fineshed")
#инструкция continue - переводит выполнение на начало цикла
i = 0
while True:
    i = i + 1 # или i += 1
    if i == 2:
        print("Skipping 2")
        continue
    if i == 5:
        print("brealing")
        break
    print(i)
print("Finished")