#Что вернет эта программа? (2)
nums = {1, 2, 3, 4, 5, 6}
nums = {0, 1, 2, 3} & nums
nums = filter(lambda x: x>1, nums)
print(len(list(nums)))

#Что вернет эта программа? (8)
def power(x, y):
    if y == 0:
        return 1
    else:
        return x * power(x, y - 1)
print(power(2,3))

#Рассчитайте x*(x+1) через анонимную функцию для числа 6
a =(lambda x: x*(x + 1)) (6)
print(a)

#В списке должны остаться только четные числа
nums = [1, 2, 8, 3, 7]
res = list(filter(lambda x: x%2 == 0, nums))
print(res)

#Вернуть элементы множества a, которых нет в множестве b
a = {0, 1, 2, 1, 3, 5, 4,}
b = {4, 1, 2, 3}
print(a - b)