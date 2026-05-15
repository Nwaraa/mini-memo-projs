words = ['This' , 'is' , 'a' , 'list']

for i in words:
    print(i)
# this (etnter) is (enter) a (enter) list.

#----------------------------------------------
numbers = [3 , 1, 4 , 1 , 5, 9, 2, 6, 5,]
new_numbers = []
for i in numbers:
    new_numbers += [i * 2]
print(new_numbers)
# doubles numbers
#---------------------------------------------
numbers = [3 , 1, 4 , 1 , 5, 9, 2, 6, 5,]
big = []
for i in numbers:
    if i > 5: #bigger den 5 
        big.append(i)
print(big)
#prints biggers than a certian number !!
things = ['This' , 'is' , 'a' , 'list']
thing_to_find = 'iss'
found= False
for thing in things:
    if thing == thing_to_find:
        found = True
        break
print(found)
#to foind a specific element in a list n check if thats there
#-------------------------------------------
