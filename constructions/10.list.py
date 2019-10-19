#работа со списками
words = ["Hello", "world", "!"]
print(words[0])
print(words[1])
print(words[2])

#простой пример
nums = [5,4,3,2,1]
print(nums[1])

#пустой список
empty_list = []
print(empty_list)

#разные типы элементов списка
number = 3
things = ["string", 0, [1, 2, number], 4.56]
print(things[0])
print(things[1])
print(things[2])
print(things[2] [2])
print(things[2] [0])

#при вызове несуществующего элемента из списка будет ошибка IndexErorr;  При индексации целых чисел будет ошибка TypeErorr
str = "Hello world!"
print(str[7])