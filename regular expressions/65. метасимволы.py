'''
Среди других метасимволов: *, +, ?, { и }.
С их помощью задается число упоминаний.
Метасимвол * означает «ноль или более упоминаний объекта поиска». Это команда найти как можно больше упоминаний.
«Объект поиска» указывается в скобках; им может быть один символ, класс или группа символов.
'''
import re

pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
    print("Match 1")

if re.match(pattern, "eggspamspamegg"):
    print("Match 2")

if re.match(pattern, "spam"):
    print("Match 3")

#будут найдены строки, начинающиеся с комбинации «egg», за которой следует (или нет) неограниченное число упоминаний «spam».

#Метасимвол + очень похож на * с тем отличием, что он означает «одно (или более) упоминание», в отличие от «ноль или более упоминаний».
import re

pattern = r"g+"

if re.match(pattern, "g"):
    print("Match 1")

if re.match(pattern, "gggggggggggggg"):
    print("Match 2")

if re.match(pattern, "abc"):
    print("Match 3")
# * означает ноль или более упоминаний предшествующего выражения
# + означает одно (или более) упоминание предшествующего выражения
# ? означает «ноль повторений или одно повторение».
import re

pattern = r"ice(-)?cream"

if re.match(pattern, "ice-cream"):
    print("Match 1")

if re.match(pattern, "icecream"):
    print("Match 2")

if re.match(pattern, "sausages"):
    print("Match 3")

if re.match(pattern, "ice--ice"):
    print("Match 4")

#найти "color" и "colour"
pattern = r"colo(u)?r"
'''
Фигурные скобки можно использовать для поиска числа упоминаний между двумя числами.
Выражение {х, у} означает «упоминания объекта поиска между х и у».
Следовательно, {0,1} - то же самое, что ?.
Если первое число отсутствует, программа считает, что это число ноль. Если второе число отсутствует, программа будет искать до бесконечности.
'''
import re

pattern = r"9{1,3}$"

if re.match(pattern, "9"):
    print("Match 1")

if re.match(pattern, "999"):
    print("Match 2")

if re.match(pattern, "9999"):
    print("Match 3")

#"9{1,3}$" соответствует строкам с 1 - 3 девяток.