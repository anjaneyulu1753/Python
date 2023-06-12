s="anji kishore dhanu selva"
a=""
j=s.count(" ")
for k in range(0,j):
    i = s.index(" ")
    a = s[:i] +" "+ a
    s = s[i + 1:]
a = s +" "+ a
print(a)