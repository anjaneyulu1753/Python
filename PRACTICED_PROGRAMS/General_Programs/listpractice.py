a= [2,8,4,3,6,879,585,8596,8599,95,586,96,6,6895,76]
#for i in range(0,len(list1)):
   # if list1[i] > 100:
        #del list1[i]
       # i=i-1


b = []
c = []
for x in a:
    if x>=100:
        a.remove(x)
        print(a)
    else:
        c.append(x)
print(b,c)
print(a)

