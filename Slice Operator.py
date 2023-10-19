fruits = ['apples', 'pears', 'strawberries','bananas','mangoes']
text = 'Hello, I am learning python'

print(fruits[1:2])
print(fruits[0:])
print(fruits[:])
print(fruits[:1])
print(fruits[:1:2])
print(fruits[::])
print(fruits[2:4:2])
print(fruits[2::2])
print(fruits[-1])
print(fruits[-1:0])
print(fruits[-1:0:-1])

fruits.append('blueberries')
print(fruits)

# use insert instead to add blueberries where you wish to add it to
fruits[0:0] = 'b'
fruits[1:1] = 'd'
fruits[2:2] = 'c'
fruits[5:5] = 'a'
print(fruits)