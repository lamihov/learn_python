#функции списков. append - добавление элемента в конец списка
nums = [1, 2, 3]
nums.append(4)
print(nums)
#пример .append
words = ["hello"]
words.append("world")
print(words[1])
#функции списков. len - подсчет элементов списка
nums = [1, 3, 5, 2, 4]
print(len(nums))
#пример .len
letters = ["a", "b", "c"]
letters.append("d")
print(len(letters))
#функции списков. insert - вставка нового элемента на любую позицию списка
words = ["Python", "fun"]
index = 1
words.insert(index, "is")
print(words)
#пример .insert
nums = [9, 8, 7, 6, 5]
nums.append(4)
nums.insert(2, 11)
print(len(nums))
print(nums)
#функции списков. index - выводит индекс элемент в списке, при повторении элементов выводит первое упоминание
letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))
print(letters.index('p'))