s="yyyyouuuuuhojhttttttttuy HELLO HI LLL DJD JJyyy"
a=s[0]
for i in range (1,len(s)):
    if s[i-1] != s[i]:
        a = a + s[i]
print(a)



'''str1 = "aswabcdefgh"
str2 = "xsaberabcdwd"
Empty_list = []
for i in range(0,len(str1)):
    for j in range(i+1,len(str1)+1):
        if str1[i:j] in str2:
            Empty_list.append(str1[i:j])
print(Empty_list)'''
'''
str1 = "abcefgh"
str2 = "xsaerabcdwd"
str3 = ""
for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i:i+4] == str2[j:j+4]:
            str3 += str1[i:i+4]
print(str3)

'''