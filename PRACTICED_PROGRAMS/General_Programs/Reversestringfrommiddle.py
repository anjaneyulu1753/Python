new_string = input("Enter a string: ")
print("Given input:", new_string)
l=int(len(new_string)/2)
b=new_string[0:l]
c=new_string[(l):]
print(c)
c=c[::-1]
a=b+c
print(a)

## OUTPUT:
#Enter a string: counting
#Given input: counting
#ting
#coungnit

