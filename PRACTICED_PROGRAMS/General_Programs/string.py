s="youuuuuhojhttttttttuy HELLO HI LLL DJD JJy"
l=len(s)
a=""
for i in range (0,l):
    if i>0:
        if s[i-1] != s[i]:
            a = a + s[i]
    elif s[i]!=s[i+1]:
        a = a + s[i]
print(a)
########## List Comprehension Method
#b="".join([s[i] for i in range(0,l) if s[i-1]!=s[i] ])
#print("without repeated letters= ",b)

