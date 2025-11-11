import string
def first_word(text):
    punctuation = string.punctuation
    punctuation = punctuation.replace("'", "")
    for p in punctuation:
        if p in text:
            text = text.replace(p, " ")
    text = text.split()
    return text[0].strip(" ")
    # punctuation = string.punctuation
    # punctuation = punctuation.replace("'","")
    # if len(text) == 0:
    #     return "nothing"
    # list2 = list(text)
    # for p in punctuation:
    #     if p in list2:
    #         list2.remove(p)
    # text = ''.join(list2)
    # list1 = text.split(" ")
    # first_word1 = list1[0]
    # print(first_word1)
    # # for i in range(len(list1)):
    # #     for l in punctuation:
    # #         if l not in list1[i]:
    # #             first_word1 = str(list1[i])
    # #             continue
    # #     for p in punctuation:
    # #         if list1[i][-1] == p:
    # #             list1[i] = list1[i][:-1]
    # #             print(first_word1)
    # #             print(p)
    # #             continue
    # #         elif list1[i][0] == p:
    # #             first_word1 = list1[i][1:]
    # #         else:
    # #             continue
    # return first_word1
first_word(".., and so on ...")
assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
