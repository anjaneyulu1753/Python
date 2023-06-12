string="NAGANJANEYULU GUDAPATI MSYS TECHNOLOGIES"
a=list(string)
count=0
print(a)
b=list(dict.fromkeys(a))
print(b)
for i in range(len(b)):
    if b[i]!=" ":
        if b[i] in string:
            count=string.count(b[i])
        print(b[i],":",count, "times")

