def popular_words(text, list1):
    text = text.lower().split()
    result = {}
    for i in list1:
        result[i] = text.count(i.lower())
    return result
    # lenght1 = len(list1)
    # # amount_l = []
    # dictionary1 = {}
    # text = text.lower()
    # # for i in range(lenght1):
    # #     list1[i] = list1[i].lower()
    # #     amount_l.append(text.count(list1[i]))
    # for i in range(lenght1):
    #     if list1[i] not in text:
    #         dictionary1[list1[i]] = 0
    #         continue
    #     index = text.index(list1[i])
    #     print(list1[i])
    #     print(index)
    #     index-=1
    #     if text.find(str(index)) != ' ':
    #         dictionary1[list1[i]] = 0
    #         continue
    #     print(index)
    #     index += len(list1[i]) +1
    #     if text.find(str(index)) != ' ':
    #         dictionary1[list1[i]] = 0
    #         continue
    #     print(index)
    #     dictionary1[list1[i]] = text.count(list1[i])
    #     print(dictionary1)
    # print(dictionary1)
# popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near'])
assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
