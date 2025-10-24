import string
import keyword
capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cap_list = list(capitals)

print(cap_list)
while True:
    user_input = input("Enter an int name: ")
    if user_input =="":
        print("Please write the name of the int")
        print("False")
        continue
    if user_input[0].isdigit():
        print("The name cannot start with a number")
        print("False")
        continue
    has_capital = False
    for i in user_input:
        if i in cap_list:
            has_capital = True
    if has_capital:
        print("The name can't have capital letters")
        print("False")
        continue
    list1 = list(string.punctuation)
    list1.remove("_")
    has_punctuation = False
    for i in user_input:
        if i in list1:
            has_punctuation = True
    if has_punctuation:
        print("The name can't have punctuation")
        print("False")
        continue
    if "__" in user_input:
        print("False")
        continue
    if " " in user_input:
        print("The name cannot contain spaces")
        print("False")
        continue
    if user_input in keyword.kwlist:
        print("The name cannot contain keywords")
        print("False")
        continue
    else:
        print("True")
        break
    # else:
    #     print("The name is", user_input)
    # print(user_input)
