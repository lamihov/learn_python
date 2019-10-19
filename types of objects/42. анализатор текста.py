#Рассмотрим программу которая анализирует файл и определяет, какой процент текста приходится на каждый символ.
filename = input("Enter a filename: ")
with open(filename) as f:
    text = f.read()
print(text)

#Заполните пропуски так, чтобы содержимое читалось с помощью инструкции with
with open(filename) as f:
    tex = f.read()

#Определяется функция, которая подсчитывает сколько раз символ встречается в тексте
def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

#В качестве аргументов функции присвоены текст файла и один символ; функция возвращает число упоминаний символа в тексте
filename = input("Enter a filename")
with open(filename) as f:
    text = f.read()
print(count_char(text, "r"))

#Часть программы находит какой процент приходится на каждый из символов алфавита
for char in "abcdefghijklmnopqrstuvwxyz":
    perc = 100 * count_char(text, char) / len(text)
    print("{0} - {1}".format(char, round(perc, 2)))

#Полный листинг программы
def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count
filename = input("Enter a filename")
with open(filename) as f:
    text = f.read()
for char in "abcdefghijklmnopqrstuvwxyz":
    perc = 100 * count_char(text, char) / len(text)
    print("{0} - {1}".format(char, round(perc, 2)))