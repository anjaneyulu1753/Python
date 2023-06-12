s="ABCDCDC"
a="CDC"
c=[]
b=len(a)
for i in range(len(s)-(b-1)):
    c.append(s[i:i+b])
print("substring in : ",c.count(a), "times")