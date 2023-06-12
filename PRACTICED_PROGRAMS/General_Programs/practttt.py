#string="Hi helloooooooooo how are you hi hello youuuuuuuuuuuu"
string="youuuuuy"

a=[]
for i in string:
    a.append(i)
a=list(dict.fromkeys(a))
b="".join(a)
print(a)
print(b)

