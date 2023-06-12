num=108
if num>1:
    for i in range(2,int(num/2)+1):
        if (num%2==0):
            print("given number is not prime")
            break
    else:
        print("given number is prime")
else:
    print("given number is not prime")
