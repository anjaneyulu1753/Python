num = int(input("Enter any positive number: "))
temp=num
rev=0
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
if temp==rev:
    print("The given value is a palindrome")
else:
    print("The given value is not palindrome")