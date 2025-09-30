import random
a=random.randint(1,10)
b=int(input("Enter a number between 1 and 10"))
if a==b:
    print("You are right")
else:
    print("You are wrong")
    print("The number was", a)
