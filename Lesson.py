import keyword
input1=  input("Enter the input: ")
if input1 in keyword.kwlist:
    print("Hello")
elif "__" in input1:
    print("Hello")