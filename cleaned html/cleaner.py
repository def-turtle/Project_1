def cleaner(file1):
    file = open(file1, 'r')
    no_html = open("text.txt", 'w')
    html = file.read()
    while True:
        b = html.find(">")
        a = html.find("<", b)
        if a == -1 or b == -1:
            break
        no_html.write(html[b+1:a].strip() + "\n")
        html = html[a+1:]
    file.close()
    no_html.close()
    file1 = open("text.txt", "r")
    c = file1.read()
    list1 = list(c)
    list2 = ["\n", ">", "<"]
    list3 = []
    for i in list1:
        if i not in list2:
            list3.append(i)
    f = open("text.txt", "w")
    a = """"""
    for i in list3:
        if i == " ":
            a += "\n"
            continue
        a+=i

    f.write(a)
    f.close()
    print(list3)
cleaner("index.html")
