


digits = ['2','3']
Dict= {  "2":["a","b","c"],
         "3":["d","e","f"],
         "4":["g","h","i"],
         "5":["j","k","l"],
         "6":["m","n","o"],
         "7":["p","q","r","s"],
         "8":["t","u","v"],
         "9":["w","x","y","z"]
      }
result=[]
array=[]
letters=Dict[digits[0]]
for i in letters:
    array.append(i)
    #combine(index+1,array)
    print(array)
    array.pop()
    print(array)
print(array)
#for x in digits:

    #if i in letters:
        #print((x))
#if x in range:
 #   if i in range (x):
  #      print(x,i)
"""for x in range(0, len(digits)-1):
    for i in range (0, len(letters)-1):
        if digits[x]==letters[i]:
            print(x)"""

