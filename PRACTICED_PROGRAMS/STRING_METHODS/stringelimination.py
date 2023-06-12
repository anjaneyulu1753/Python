string="the lyrics is poor"

sub="not"
sub1="poor"
a=string.split()
#print(a)
b=""
if sub in a:
    a.remove(sub)
    b=" ".join(a)
    print(b)
if sub1 in string:
    c=b.replace(sub1,"good")
    print(c)
