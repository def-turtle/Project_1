import math
list1 = [1,2,3]
list1_len = len(list1)
amount = math.ceil(list1_len/2)
list2 = list1[amount:]
list3 = list1[:amount]
new_list = [list3,list2]
print(new_list)
