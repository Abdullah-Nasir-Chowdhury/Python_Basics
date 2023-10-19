# there are 2 main types of for loops,
# type1: iteration by indices
# for x in range(0,10):
#     print(x)

# type2: iteration by items
fruits = ['apples','mangoes','pears','strawberries']
for fruit in fruits:
    print(fruit)
for fruit in fruits:
    if fruit == 'pears':
        print(fruit)
    else:
        print('not pears')

# type1:
for x in range(len(fruits)):
    if fruits[x] == 'pears':
        print(fruits[x])
    else:
        print('not a pear')