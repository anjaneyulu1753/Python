new_string = input("")
print("Given input:", new_string)
l=int(len(new_string)/2)
b=new_string[0:l]
c=new_string[(l):]
print(c)
c=c[::-1]
a=b+c
print(a)
