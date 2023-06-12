string="Naganjaneyulu gudapati"
sub=input("Enter a string: ")
c=""
i=string.find(sub)
a=string[(i+1):]
print(a)
b=string.split(sub,1)
print(b[1])


for i in range(0,len(string)):
    if string[i]==sub:
        for j in range(i+1,len(string)):
            c=c+string[j]
        break
print(c)