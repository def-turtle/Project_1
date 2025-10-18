
list_1 = [0]
for i in list_1:
    first_num = int(input("Enter the first number: "))
    operator = input("Enter the operator: ")
    second_num = int(input("Enter the second number: "))
    first_type = type(first_num)
    second_type = type(second_num)
    if first_type!= int:
        print("First number must be an integer")
        first_num = int(input("Enter the first number: "))
    elif second_type!= int:
        print("Second number must be an integer")
        second_num = int(input("Enter the second number: "))
    elif operator == "+":
        result = first_num + second_num
        print(result)
    elif operator == "-":
        result = first_num - second_num
        print(result)
    elif operator == "*":
        result = first_num * second_num
        print(result)

    elif operator == "//":
        result = first_num // second_num
        print(result)
    elif operator == "**":
        result = first_num ** second_num
        print(result)
    elif operator == "%":
        result = first_num % second_num
        print(result)
    elif operator == "/":
        if second_num == 0:
            print("Enter a number greater than 0")
        else:
            result = first_num / second_num
            print(result)
    else:
        print("Invalid operator")
    a = input("Do you want to continue? yes or no: ")
    if a == "yes":
        list_1.append('1')
    else:
        break
