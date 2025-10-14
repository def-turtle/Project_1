import math
list1 = [1,2,3,4,5,6,232]
list2 = []
list3 = []
list1_len = len(list1)
amount = math.ceil(list1_len/2)
list2 = list1[amount:]
list3 = list1[:amount]
print(list3,list2)