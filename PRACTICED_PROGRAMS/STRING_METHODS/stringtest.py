a="ABCDCDC"
sub="CD"
l=len(sub)
i=a.find(sub)
print(i)
for x in range(0,i+l):
    count=a.count(sub)
#for x in range(i+1,len(a)):
        #c=a.count(sub)
#count=count+c
print(count)