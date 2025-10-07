# import random
# a=random.randint(1,10)
# c=6
# for i in range(1,6):
#     c-=1
#     print("You have", c ,"tries left")
#     b = int(input("Enter a number between 1 and 10: "))
#     if a == b:
#         print("You guessed right")
#         break
#     else:
#         print("You are wrong")
#     if c == 1:
#         print("You didn't guess right, the right number was", a)
#         break
import math
a = int(input('Введіть 5-ти значне число: '))
reversed_num = int(str(a)[::-1])
b = len(str(a))
if b == 5:
    print(reversed_num)
else:
    print("Not a 5 digit number.")
