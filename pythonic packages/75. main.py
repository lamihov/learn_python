'''По большей части код языка Python - это либо импортируемый модуль, либо сценарий с некоторой функциональностью.
Тем не менее, иногда лучше сделать файл, который может быть импортирован как модуль и запущен как сценарий.
Для этого поместите код сценария внутрь if __name__ == "__main__".
Так он не будет запущен при импортировании файла
'''

def function():
    print("This is a module function")

if __name__=="__main__":
    print("This is a script")

'''Если мы сохраним код из предыдущего примера в файл с именем sololearn.py, мы можем затем импортировать его в другой сценарий как модуль по имени sololearn.
sololearn.py'''
#sololearn.py
def function():
    print("This is a module function")

if __name__=="__main__":
    print("This is a script")
#some_script.py
import sololearn

sololearn.function()