a = int(input("Enter a number: "))
first_num = a//1000
second_num = (a%1000)//100
third_num = (a%1000)//10-(second_num*10)
forth_num =(a%1000)-(third_num*10+second_num*100)
# second_num = a//100
# third_num = a//10
b=len(str(a)[::-1])
if b==4:
    print(first_num)
    print(second_num)
    print(third_num)
    print(forth_num)
else:
    print("You had to type in a four digit number")
