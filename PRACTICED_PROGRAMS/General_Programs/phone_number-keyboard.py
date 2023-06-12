x,y,z=str(input("Please Enter the values: "))

digits={
'2':['a','b','c'],
'3':['d','e','f'],
'4':['g','h','i'],
'5':['j','k','l'],
'6':['m','n','o'],
'7':['p','q','r','s'],
'8':['t','u','v'],
'9':['w','y','z']

}
c=[]
m=digits.get(x)
n=digits.get(y)
o=digits.get(z)
for i in range(0,len(m)):

    for j in range(0,len(n)):
        for k in range(0,len(o)):
            c.append(m[i]+n[j]+o[k])
print("The Combination is : ",c)
