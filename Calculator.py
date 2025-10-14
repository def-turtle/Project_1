first_num = int(input("Enter the first number: "))
operator = input("Enter the operator: ")
second_num = int(input("Enter the second number: "))
if operator == "+":
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