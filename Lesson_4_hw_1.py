import random
amount = random.randint(3,10)
listShow = []
for i in range(amount):
    randomNumber = random.randint(0, 100)
    listShow.append(randomNumber)
    i+=1
    # random_list = random.randint(0, 100)
    # if i==0:
    #     print("[",random_list, end=",", sep="")
    #     continue
    # elif i==9:
    #     print(random_list, end="]", sep="")
    #     continue
    # else:
    #     print(random_list,end=",", sep="")

print(listShow)