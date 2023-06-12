z = list((input("Please Enter Two values: ")))

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

if len(z)<2:

    x=z[0]
    m = digits.get(x)
    print(m)

else:
    x=z[0]
    y=z[1]


    m = digits.get(x)
    n = digits.get(y)
    c = []
    for i in range(0, len(m)):
        for j in range(0, len(n)):
            c.append(m[i] + n[j])

    print("The Two Combinations are : ", c)