"""
Name : GUDAPATI NAGANJANEYULU,
Date : 04-May-2023.
"""



## Extract elements with frequency greater than K


#  Extract all elements whose frequency is greater than 'K' in given a List,  here K =3

###   *********** ALGORITHM  ************ 

"""
Step 1--> Take a new list with consist of duplicate values.
Step 2--> Initiate 'K' value & create a another new empty list for result.
Step 3--> Use for loop to iterate over the items.
Step 4--> count the duplicate values exists in the list using count command and assign to variable 'a'
Step 5--> Add the values to new list with frequency greater than 'K' using 'if' condition.
Step 6--> Print the Extracted new list.
"""



# *******************   PROGRAM -- 1 *****************

test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k=3
new_list = []
for i in test_list:
    a=test_list.count(i)
    if a>k:
        if i not in new_list:
            new_list.append(i)
print("Extracted list: ", new_list)

##    O/P:  Extracted list:  [4, 3]


######## ******************************        *******************



## Extract all elements whose frequency is greater than 'K' in given a List,  here K =2

###   *********** ALGORITHM  ************ 



"""
Step 1--> Take a new list with consist of duplicate values.
Step 2--> Initiate 'K' value & create a another new empty list for result.
Step 3--> Use for loop to iterate over the items.
Step 4--> count the duplicate values exists in the list using count command and assign to variable 'a'
Step 5--> Add the values to new list with frequency greater than 'K' using 'if' condition.
Step 6--> Print the Extracted new list.
"""



# ********************** PROGRAM -- 2 *********************

test_list = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6]
k=2
new_list = []
for i in test_list:
    a=test_list.count(i)
    if a>k:
        if i not in new_list:
            new_list.append(i)
print("Extracted list : ", new_list)

##  O/P:  Extracted list:  [4, 6, 3]


#### ********************** THANK YOU *************************