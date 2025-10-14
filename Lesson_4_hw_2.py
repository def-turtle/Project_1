user_input = int(input("Enter a few number: "))
list1 = list(map(int, str(user_input)))
lastItem = list1[-1] #6
answear = 0
for index,x in enumerate(list1):
    if index%2 ==0:
        answear += x*lastItem
print(answear)