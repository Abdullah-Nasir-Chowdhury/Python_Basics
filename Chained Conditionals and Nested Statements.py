# chained conditionals is using words like and, or

x = 3
y = 10

if x == y and x+y == 13:
    print('and statement ran')
if x == y or x+y == 13:
    print('or statement ran')
if not(x == y and x+y == 13):
    print('not statement ran')

if x == 2:
    if y == 10:
        print('x=3, y=10')
    else:
        print('y!=10')
else:
    print('x!=2')