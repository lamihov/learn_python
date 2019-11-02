'''
Регулярные выражения - средство для работы со строками.
Главным образом они используются для выполнения двух задач:
- чтобы проверить, соответствует ли строка определенному набору символов (например, имеет ли строка формат адреса электронной почты)
- когда нужно выполнить замену внутри строки (например, исправить правописание слова во всех его упоминаниях).
Регулярные выражения в Python создаются с использованием модуля re, входящего в стандартную библиотеку.
После того как вы определили регулярное выражение, с помощью функции re.match можно определить, есть ли совпадение в начале строки.
Если совпадение найдено, match возвращает объект совпадения; в противном случае возвращает None.
'''

import re
pattern = r"spam"

if re.match(pattern, "spamspamspam"):
    print("Match")
else:
    print("No match")
'''
- Функция re.search используется для поиска набора символов в любом месте строки.
- Функция re.findall возвращает список всех подстрок, которые совпадают с искомым набором символов.
'''
import re

pattern = r"spam"

if re.match(pattern, "eggspamsausagespam"):
    print("Match")
else:
    print("No match")

if re.search(pattern, "eggspamsausagespam"):
    print("Match")
else:
    print("No match")

print(re.findall(pattern, "eggspamsausagespam"))

'''
Поиск с регулярными выражениями возвращает объект с несколькими методами, содержащими информацию об объекте.
Это такие методы, как:
- group, возвращающий совпавшую строку,
- start и end, возвращающие начальную и конечную позицию первого совпадения, 
- span, возвращающий начальную и конечную позицию первого совпадения в виде кортежа.
'''

import re

pattern = r"pam"

match = re.search(pattern, "eggspamsausage")
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())

#вернуть начальную и конечную позицию совпадения
import re

pattern =r"test"

match = re.search(pattern, "some test")
print(match.start())
print(match.end())

#Один из наиболее важных методов re, используемых в регулярных выражениях, метод sub.
re.sub(pattern, repl, string, count=0)

'''Этот метод заменяет все упоминания набора символов в строке на repl: заменяются все упоминания, если не установлено ограничение count. 
Метод возвращает новую версию строки.'''

import re

str = "My name is David. Hi David."
pattern = r"David"
newstr = re.sub(pattern, "Amy", str)
print(newstr)

#пример
import re
num = "07987549836"
pattern = r"9"
num = re.sub(pattern, "0", num)
print(num)