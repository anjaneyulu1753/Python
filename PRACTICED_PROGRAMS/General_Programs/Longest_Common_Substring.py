s="abcdefgh"
s1="xswerabcdwd"
l=len(s)
a=[]
for i in range(1,l+1):
    for j in range(0,l-(i-1)):
        a.append(s[j:(j+i)])
d=[]
for i in a:
    if i in s1:
        d.append(i)
print("common Strings: ",d)
print("longest common string: ", d[-1])