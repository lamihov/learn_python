''' Генераторы - интерируемый тип, как списки или кортежи. В отличие от списков им нельзя присваивать произвольные индексы, но они поддерживают циклы for.
Создаются с использованием yield (возвращает значение из генератора).'''
def countdown():
    i = 5
    while i > 0:
        yield i
        i -= 1
for i in countdown():
    print(i)

'''Генераторы возвращют по одному элементу за раз, не имеют ограничение по памяти - могут выполняться бесконечно'''
def infinite_sevens():
    while True:
        yield 7
for i in infinite_sevens():
print(i)

#пример: генератор простых чисел, который возвращает все простые числа цикла
def get_primes():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num +=1

'''Конечные генераторы могут быть преобразованы в списки, для этого их нужно передать как аргументы функции list.'''
def numders(x):
    for i in range(x):
        if i%2 == 0:
            yield i
print(list(numders(11)))

#пример
def make_word():
    word= ""
    for ch in "spam":
        word +=ch
        yield word
print(list(make_word()))