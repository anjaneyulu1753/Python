
#Name : Gudapati Naganjaneyulu,
#Date : 05-May-2023.

## Letter Combinations of a phone number

num = list((input("Please Enter input value: ")))

digits = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'y', 'z']

}
c = []

if len(num)==1:

    x=num[0]
    m = digits.get(x)
    print("The single number combination is : ",m)

elif len(num)==2:
    x = num[0]
    y = num[1]

    m = digits.get(x)
    n = digits.get(y)
    for i in range(0, len(m)):
        for j in range(0, len(n)):
            c.append(m[i] + n[j])

    print("The Two numbers Combinations are : ", c)
elif len(num)==3:
    x = num[0]
    y = num[1]
    z = num[2]

    m = digits.get(x)
    n = digits.get(y)
    o = digits.get(z)
    for i in range(0, len(m)):

        for j in range(0, len(n)):
            for k in range(0, len(o)):
                c.append(m[i] + n[j] + o[k])
    print("The Three numbers Combinations are : ", c)
elif len(num)<1:
    print(c)
else:
    print("The given input is invalid.")

#OUTPUT:
#Please Enter input value: 456
#The Three numbers Combinations are :  ['gjm', 'gjn', 'gjo', 'gkm', 'gkn', 'gko', 'glm', 'gln', 'glo', 'hjm', 'hjn', 'hjo', 'hkm', 'hkn', 'hko', 'hlm', 'hln', 'hlo', 'ijm', 'ijn', 'ijo', 'ikm', 'ikn', 'iko', 'ilm', 'iln', 'ilo']
