string = "hi hello how are you how hello"
a=string.split()
print(a)
a=list(dict.fromkeys(a))
print(a)
for i in range(len(a)):
    if a[i] in string:
        b=string.count(a[i])
        print("The term : ", a[i],",is:",b)