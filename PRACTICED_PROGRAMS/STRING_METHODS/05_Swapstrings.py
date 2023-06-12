string1 = "abc"
string2 = "xyz"    # output: "xyc abz"
a=string2[:2]+string1[2:]
b=string1[:2]+string2[2:]
c=a+" "+b
print(c)

