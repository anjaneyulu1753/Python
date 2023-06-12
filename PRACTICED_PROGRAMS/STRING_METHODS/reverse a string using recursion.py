def recursion(string):
    print(string)

    if len(string)==8:
        return string
    else:
        return recursion(string[1:])+string[0]



print(recursion("anjaneyulu"))

