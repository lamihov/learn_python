'''Декораторы предназначены для изменения поведения фнукции без ее модификации'''
def decor(func):
    def wrap():
        print("=====")
        func()
        print("=====")
    return wrap
def print_text():
    print("Hello world!")
decorated = decor(print_text)
decorated()

''' В предыдущем примере, декорировали функцию заменив ее переменную содержащую функцию, на "обернутую" версию"'''
def print_text():
    print("Hello word!")
print_text = decor(print_text)
#Если определена функция, ее можно декорировать добавив @:
@decor
def print_text():
    print("Hello word!")