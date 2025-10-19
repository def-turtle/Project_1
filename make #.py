a = input("Please enter something: ")
b = a.title()
clean = ''
list1 = [",",".","?","!","1","2","3","4","5","6","7","8","9","0"]
clean = b.replace(" ", "")
for i in list1:
    clean = clean.replace(i,"")
clean = "#"+clean
lenght1 = len(clean)
if lenght1 > 140:
    clean = clean[:140]
print(clean)