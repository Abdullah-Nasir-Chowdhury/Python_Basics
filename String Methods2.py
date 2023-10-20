# .find(), .count(), .replace()
string = 'hellow'
print(string.find('o'))
print(string.find('w'))
print(string.find('10')) # there is no 10, so you get -1


print(string.count('l'))
print(string.count('hello'))

# remove words or spaces:
name = 'Abdullah Nasir Chowdhury'
print(name)
name = name.replace(' ','')
print(name)

string_new = 'body_count'
if string_new.count('_') > 0:
    string_new = string_new.replace('_','')
print(string_new)
