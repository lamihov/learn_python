# переназначение элемента списка по индексу
nums = [7, 7, 7, 7, 7,]
nums[2] = 5
print (nums)

#операции над списками
nums = [1, 2, 3, 4]
print(nums + [5, 6, 7])
print(nums * 3)

#Проверка на наличие элемента в списке "in"
words = ["spam", "egg", "spam", "sausage"]
print ("spam" in words)
print("egg" in words)
print("tomato" in words)

#пример на наличие элемента в списке
nums = [10, 9, 8, 7, 6, 5]
nums[0] = nums[1] - 5
if 4 in nums:
    print(nums[3])
else:
    print(nums[4])

#проверка на отсутствие элемента в списке
nums = [1, 2, 3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)