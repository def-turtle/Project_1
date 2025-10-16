a = input("Please enter something: ")
b = ''
split = a.split(" ")
for i in split:
    if i[0].islower():
        upper = i[0].upper() + i[1:]
        b+=upper
        continue
    b+=i
print(b)
clean = ''
clean = b.replace(" ", "")
clean = clean.replace(",", "")
clean = clean.replace("!", "")
clean = clean.replace("?", "")
clean = clean.replace("1", "")
clean = clean.replace("2", "")
clean = clean.replace("3", "")
clean = clean.replace("4", "")
clean = clean.replace("5", "")
clean = clean.replace("6", "")
clean = clean.replace("7", "")
clean = clean.replace("8", "")
clean = clean.replace("9", "")
clean = clean.replace("0", "")
clean = "#"+clean
lenght = len(clean)

if lenght > 140:
    clean = clean[:140]
print(clean)