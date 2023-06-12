num=int(input("Please enter any number: "))
temp=num
arm=0
l=len(str(num))
while num>0:
    rem=num%10
    arm=arm+rem**l
    num=num//10
if temp==arm:
    print("The given number is armstrong")
else:
    print("the given number is not armstrong")