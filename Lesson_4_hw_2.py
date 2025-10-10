user_input = int(input("Enter a few number: "))
list1 = list(map(int, str(user_input)))
lastItem = list1[-1] #6
answer = 0
for x in list1:
    index1 = list1.index(x)
    even_index = index1 % 2 == 0
    if even_index:
        answer += x*lastItem
    # if x.__index__()%2==0:
    #     newList.append(x*lastItem)
print(answer)