s="anji kishore dhanu selva"
a=""
j=s.count(" ")
for k in range(0,j):
    i = s.index(" ")
    a = a+" "+"".join(sorted(s[:i]) )
    s = s[i + 1:]
a = a+" "+"".join(sorted(s))
print(a)