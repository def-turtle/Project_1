import random
a=random.randint(1,10)
c=6
for i in range(1,6):
    c-=1
    print("You have", c ,"tries left")
    b = int(input("Enter a number between 1 and 10: "))
    if a == b:
        print("You guessed right")
        break
    else:
        print("You are wrong")
    if c == 1:
        print("You didn't guess right, the right number was", a)
        break
