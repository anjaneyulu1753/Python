num=int(input("Enter any number: "))
l=len(str(num))
temp=num
pal=0
while num>0:
    rem=num%10
    pal=pal*10+rem
    num=num//10
if temp==pal:
    print("palindrome")
else:
    print("not palindrome")
