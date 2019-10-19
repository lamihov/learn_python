#тест по конструкциям
list = [1, 1, 2, 3, 5, 8, 13]
print(list[list[4]])
#----
for i in range(10):
    if not i % 2 == 0:
        print(i + 1)
#------
while False:
    print("Looping")
#программа должна вывести первый элемент списка, если список содержит четное количество элементов
list = [1, 2, 3, 4]
if len(list) % 2 == 0:
    print(list[0])
#-----
letters = ['x', 'y', 'z']
letters.insert(1, 'w')
print(letters[2])
#программа должна перебрать все элементы списка и вывести результат
list = [1, 2, 3, 4]
for var in list:
    print(var)