string=input("enter any string: ")
temp=string[::-1]
if string==temp:
    print("given string is a palindrome")
else:
    print("given string is not a palindrome")
#rev=""
str1=""
for i in range(1,len(string)+1):
    #rev=string[i]+rev
    str1=str1+string[-i]
#print(rev)
print(str1)