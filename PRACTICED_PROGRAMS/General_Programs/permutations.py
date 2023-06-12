s="xyzy"
a=[]
for i in range(len(s)):
    for j in range(len(s)):
        for k in range(len(s)):
            a.append((s[i],s[j],s[k]))
print(a)


