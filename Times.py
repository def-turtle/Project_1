input2= int(input("Enter a number: "))
list1  = list(str(input2))
len1 = len(list1)
result = 1
for i in range(len1):
    result = int(list1[i])*result
while result>9:
    result_l = list(str(result))
    len2 = len(result_l)
    result = 1
    for i in range(len2):
        result = int(result_l[i])*result
print("Result:", result)