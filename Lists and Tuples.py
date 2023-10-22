# initiate list:
fruits = ['apple', 'pear', 3]
print(fruits)
# access individual items, indices:
print(fruits[0])
print(fruits[1])
print(fruits[2])
# access last element:
print(fruits[-1])
# add items to the list:
fruits.append('mango')
print(fruits)
# remove items from list:
fruits.pop(0)
print(fruits)
# remove last element from list:
fruits.pop()
print(fruits)
# add another list to list:
fruits.append(['jackfruit','litchii'])
print(fruits)
# manipulate data in list:
fruits[2] = 'banana'
print(fruits)
# delete:
del fruits[0]
print(fruits)
# get index of value:
a = fruits.index(3)
print(a)
# remove via index:
del fruits[a]
print(fruits)
if 'jackfruit' not in fruits:
    print("jackfruit not in fruits basket")

# sort list:
mylist = [44,5,6,71,24,6,4,4,4,4,4,8]
mylist.sort()
print(mylist)
# reverse list:
mylist.reverse()
print(mylist)
# count how many times a value appears:
print(mylist.count(4))
# check length of a list:
print(len(mylist))
# randomize elements of a list:
from random import shuffle
shuffle(mylist)
print(mylist)
# initiate tuple: used for co-ordinates, colors, rectangles,
# can't be changed!
price = (1,2,3,4,5)

