s="ABCDCDC"
a="CDC"
b=s.find(a)
count=0
if a in s:
    count+=1
    s=s[b+1:]
    if a in s:
        count+=1
    print(count)