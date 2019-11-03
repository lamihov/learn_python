'''Группа создается путем заключения части регулярного выражения в круглые скобки.
Это означает, что группа может быть задана в качестве аргумента метасимволам, таким как * и ?.
'''

import re

pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
    print("Match 1")

if re.match(pattern, "eggspamspamspamegg"):
    print("Match 2")

if re.match(pattern, "spam"):
    print("Match 3")
#(spam) представляет собой группу внутри набора символов в примере вверху

'''Содержание групп можно получить с помощью функции group.
Вызов метода group(0) или group() возвращает все найденные совпадения.
Вызов метода group(n), где n больше 0, возвращает n-ю группу, считая слева.
Метод groups() возвращает все группы, начиная с первой.'''

import re

pattern = r"a(bc)(de)(f(g)h)i"

match = re.match(pattern, "abcdefghijklmnop")
if match:
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.groups())

'''Есть несколько типов специальных групп.
Два наиболее важных: именованные группы и «незахватывающие» группы.
Формат именованных групп: (?P<name>...), где name - имя группы, а ... - содержание группы.
У них точно такая же функциональность, как и у обычных групп, но их можно получить не только по номеру, но и с помощью метода group(name).
Формат «незахватывающих» групп: (?:...). 
Их нельзя получить по методу группы, поэтому их можно добавлять в регулярное выражение, не нарушая нумерацию.
'''

import re
pattern = r"(?P<first>abc)(?:def)(ghi)" #(именнованная группа)(незахватывающая группа)

match = re.match(pattern, "abcdefghi")
if match:
    print(match.group("first"))
    print(match.groups())

#пример:
len(match.groups()) (a)(b(?:c)(d)(?:e)) #3

#другой важный метасимвол: |. Он имеет значение «или»; так в результате выражения красный|синий вернется либо «красный» или «синий».
import re

pattern = r"gr(a|e)y"

match = re.match(pattern, "gray")
if match:
    print ("Match 1")

match = re.match(pattern, "grey")
if match:
    print ("Match 2")

match = re.match(pattern, "griy")
if match:
    print ("Match 3")