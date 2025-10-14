# user_input = int(input("Enter a few number: "))
# list1 = list(map(int, str(user_input)))
list1 = [0, 0, 0, 1, 2]
print("Current list:", list1)
for i in list1:
    if i==0:
        list1.remove(i)
        list1.append(i)
print("Updated list", list1)