list1 = []
if len(list1) == 0:
    print(0)
else:
    lastItem = list1[-1]
    even = []
    for i in range(len(list1)):
        if i % 2 == 0:
            even.append(list1[i])
    result = sum(even)
    print(result*lastItem)