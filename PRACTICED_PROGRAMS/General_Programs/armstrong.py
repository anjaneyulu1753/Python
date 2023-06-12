num=int(input("Please enter the number: "))
l=len(str(num))
temp=num
arm=0
while num>0:
    rem=num%10
    arm=arm+rem**l
    num=num//10
if temp==arm:
    print("armstrong")
else:
    print("not armstrong")