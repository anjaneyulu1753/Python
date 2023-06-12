string=str(input("Enter String: "))
l=len(string)
sub="ing"
sub2="ly"
if l>=3:
    b=string[-3:]
    if b==sub:
        c=string[:-3]
        c=c+sub2
        print(c)

    else:
        d=string+sub
        print("The updated string is :",d)
else:
    print("No change in string")
