list1 = [1, 2, 3, 4, 3, 4, 2, 7]

for i in range(0, len(list1)-1):
    for j in range(i+1, len(list1)-1):
        if list1[i] == list1[j]:
            del list1[j]
print("After Removing duplicates: ", list1)
