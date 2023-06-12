def is3_letter(string):
    if len(string)<3:
        print("Original String: ",string)
    else:
        print("First three letters: ",string[:3])
is3_letter("anjaneyulu")
is3_letter("an")