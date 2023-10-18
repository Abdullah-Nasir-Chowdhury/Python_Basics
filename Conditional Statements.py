x = input('Whats your name? ')
if x == 'Abdullah':
    print('Hello, creator!')
else:
    print('Hello, friend!')
age = int(input('Whats your age!'))
if 0<age<13:
    print('you are a toddler')
elif 13<age<19:
    print('you are a teen')
elif 19<age<100:
    print('you are an adult')
else:
    print('wow, you can be that age too!')