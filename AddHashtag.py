import re
a = "I love pytho,n123!"
b = a.find("!")
d = a.find(",")
c = a.find("?")
e = a.find("1,2,3,4,5,6,7,8,9")
f = a.find(" ")
remove_items1 = "!"
remove_items2 = ","
remove_items3 = '?'
remove_items4 = " "
clean = ''
if b != -1:
    clean = a.translate(str.maketrans("","",remove_items1))
if d != -1:
    clean = a.translate(str.maketrans("","",remove_items2))
if c != -1:
    clean = a.translate(str.maketrans("","",remove_items3))
if f != -1:
    clean = a.translate(str.maketrans("","",remove_items4))
if e != -1:
    clean = re.sub(r'\d', '', a)
print(clean)