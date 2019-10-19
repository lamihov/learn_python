#словари являеются структурными данными, используются для хранения произвольных ключей
ages = {"Dave":24, "Mary": 42, "John": 58}
print(ages["Dave"])
print(ages["Mary"])
#определить словарь с двумя элементами
cars = {"BMV": "blue", "Volvo": "red"}

#попытка сослаться на ключ которого нет в словаре, вернет ошибку KeyError
primary = {
    "red": [255, 0, 0],
    "green": [0, 255, 0],
    "blue": [0, 0, 255],
}
print(primary["red"])
print(primary["yellow"]) #ошибка KeyError
#пример
test = {}
print(test[0]) #KeyError

#только объекты immutable могу быть использованы в качестве ключей словарей
bad_dict ={
    [1, 2, 3]: "one two three"
} #TypeError 