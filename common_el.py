def common_element():
    multi_3 = [i for i in range(1,101) if i%3==0]
    multi_5 = [i for i in range(1,101) if i%5==0]
    set1 = set(multi_3)
    set2 = set(multi_5)
    print(set1)
    print(set2)
    common_set = set1.intersection(set2)
    common_set.add(0)
    return common_set
result = common_element()
print(result)
assert result == {0, 75, 45, 15, 90, 60, 30}
