string="The lyrics is not that poor!"
sub="not"
sub1="poor"
sub2="good"
if sub in string:
    a=string.find("not")
    print(a)
    b=string.find("poor")
    print(b)
    if a<b:
        string=string.replace(string[14:27], "good")
        print(string)
else:
    print(string)