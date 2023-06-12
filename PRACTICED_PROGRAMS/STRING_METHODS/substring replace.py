string = "hi hello how are you"
sub_string = "how"
New_sub_string ="who"
if sub_string in string:
    c = string.replace(sub_string, New_sub_string)
    print(c)
else:
    print("Original String: ", string)

# OUTPUT
#  hi hello who are you
