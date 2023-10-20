name = input('What is your name?' )
age = input('What year were you born?: ')
try:
    name = str(name)
    print(name)
    age = int(age)
    print(age)
except:
    if ValueError:
        print('Invalid Value')



