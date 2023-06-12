a = ["Hi", "hello", "kishore", "how", "anjaneyulu","who"]
list1 = []
for i in a:
    list1.append((len(i), i))
    list1.sort(reverse=True)
print(list1)
print("word: ", list1[0][1])
print("len ", list1[0][0])


