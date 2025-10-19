while True:
    first_num = input("Enter the first number: ")
    operator = input("Enter the operator (+, -, *, /): ")
    second_num = input("Enter the second number: ")

    if first_num.isdigit() and second_num.isdigit():
        first_num = int(first_num)
        second_num = int(second_num)

        if operator == "+":
            result = first_num + second_num
        elif operator == "-":
            result = first_num - second_num
        elif operator == "*":
            result = first_num * second_num
        elif operator == "/":
            if second_num == 0:
                print("Cannot divide by zero!")
                continue
            result = first_num / second_num
        else:
            print("Invalid operator!")
            continue

        print(f"Result: {result}")
    else:
        print("Please enter valid numbers!")
        continue

    choice = input("Continue? (yes/y or no/n): ").lower()
    if choice == "no" or choice == "n":
        print("Goodbye!")
        break