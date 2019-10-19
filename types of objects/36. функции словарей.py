#новым ключам словарей можно присваивать значения
squares = {1:1, 2: 4, 3: "error", 4: 16,} #задаем значения словаря
squares [8] = 64 #присваиваем значение новому ключу
squares [3] = 9 #переназначаем значение существующего ключа
print(squares) #выводим ключе словаря

#пример
primes ={1:2, 2:3, 4:7, 7:17}
print(primes[primes[4]]) #вывести значение 4 ключа

#чтобы определить наличие ключа в словаре используется in и not in
nums = {
    1: "one",
    2: "two",
    3: "three"
}
print (1 in nums)
print ("three" in nums)
print (4 not in nums)

#Написать строку которая выводит "Yes", если ключ 112 есть в словаре "pairs"
if 112 in pairs:
    print("Yes")

#метод get - выполняет функцию индексации, но если ключ не найден в словаре он возвращает значение none
pairs = {
    1:"apple",
    "orange": [2, 3, 4],
    True: False,
    None: "True",
    }
print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345, "not in dictionary"))

#каким будет результат этих строк
fib = {1:1, 2:1, 3:2, 4:3}
print(fib.get(4, 0)) + fib.get(7, 5)