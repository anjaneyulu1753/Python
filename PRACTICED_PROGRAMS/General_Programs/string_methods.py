txt = "hello And We\tlcome to {price:.2f} my world."
x=txt.capitalize()
print(x)
a=txt.casefold()
print(a)
b=txt.center(50,'*')
print(b)
c=txt.count('e')
print(c)
d=txt.encode()
print(d)
e=txt.endswith(".")
print(e)
f=txt.expandtabs(4)
print(f)
g=txt.find("n")  # if sub string not in mani string it will give -1 default.
print(g)
h=txt.format(price=49)
print(h)
i=txt.index("n") # value not found in the main string, the index() method raises an exception.
print(i)
j=txt.isalnum()
print(j)
k=txt.isalpha()
print(k)
l=txt.isascii()
print(l)
txt1 = "1234.9"
m=txt1.isdecimal()
print(m)
n= txt1.isdigit()
print(n)
o=txt.isidentifier()
print(o)
p=txt.islower()
print(p)
q=txt.isupper()
print(q)
r=txt1.isnumeric()
print(r)
txt2="anj\i dh#fhr44#"
s=txt2.isprintable()
print(s)
t=txt.isspace()
print(t)
u=txt.istitle()
print(u)
list1=["anji", "kishore", "dhanunjay"]
v=" ".join(list1)
print(v)
txt3 = "banana"

w = txt3.ljust(50,"$")
x = txt3.rjust(50)
print(w, "is my favorite fruit.")
print(x, "is my favorite fruit.")

txt4 = ",,,,,rrttgg.....banana....rrr"

x = txt4.strip(",gr.t")

print(x)
aa=txt.startswith("h")
print(aa)
ab=txt.swapcase()
print(ab)
ac=txt.split()
print(ac)

ABC="ABCDCDC"
SUB="CDC"
ad=ABC.split(SUB)
print(ad)