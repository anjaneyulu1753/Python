string ="Anjaneyulu45as"
b="-".join(sorted(sorted(string), key=str.upper))
c=sorted(sorted(string), key=str.lower)
print(sorted(string))
print(sorted(string, reverse=True))
print(sorted(string, key=len))


print(b)
print(c)