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
elif operator == "/":
    result = first_num / second_num
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
elif second_num == 0:
    print("Please enter a number greater than zero")
else:
    print("Invalid operator")