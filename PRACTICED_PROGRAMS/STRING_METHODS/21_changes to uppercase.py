string = "AnJAneyulU"
count=0
for i in range(0,4):
    if string[i].isupper():
        count+=1
print(count)
if count>=2:
    b = string.upper()
    print(b)

