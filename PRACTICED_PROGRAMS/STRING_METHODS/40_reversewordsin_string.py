string = "Hi hello how are you"
a=string.split(" ")
#print(a)
#b=" ".join(reversed(string.split()))
#a=" ".join(a[::-1])
c=[]
for i in a:
    c.append("".join(sorted(i)))
print(" ".join(c))
