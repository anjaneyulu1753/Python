s="youuuuuhojhttttttttuy HELLO HI LLL DJD JJy"
a=s[0]
i=1
while i<len(s):
    if s[i-1] != s[i]:
        a = a + s[i]
    i+=1
print("The updated string is:",a)