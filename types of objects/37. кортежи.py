#кортежи аналогичны спискам, за исключением того, что являтся неизменяемыми
words =("spam", "eggs", "sausages")
print(words[0])

# при попытке переназначения в кортеже вызывает ошибку TypeError
words[1] = "cheese"

list = ["one", "two"] #список
dict = {1:"one", 2: "two"} #словарь
tp = ("one", "two") #кортеж

#кортеж можно создавать без использования скобок
my_tuple = "one", "two", "three"
print(my_tuple[0])

#пример
tuple = (1,(1,2,3))
print(tuple[1])