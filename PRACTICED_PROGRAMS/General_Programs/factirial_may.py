num = int(input("Enter the number up to required factorial: "))
fact=1
if num>0:
    for i in range(1,num+1):
        fact= fact*i
    print("The factorial of given is: ", fact)
else:
    print("Factorial not Possible")
    