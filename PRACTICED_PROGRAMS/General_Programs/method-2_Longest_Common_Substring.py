# Method 2 for Longest Common Sub_string
s="abcdefgh"
s1="xswerabcdwd"
sub=input("Enter any substring: ")
l=len(s)
d=[]
for i in range(l):
    for j in range(i+1,l+1):
        if s[i:j] in s1:
            d.append(s[i:j])
            j=j+1

d=sorted(d,key=len)
print("The common strings are: ",d)
if sub in d:
    if sub==d[-1]:
        print("The given substring: ",sub, "is a longest common substring.")
    else:
        print("the given substring: ", sub, "is a Common string.")
else:
    print("The given Sub_string: ", sub, "is not a common string.")