# .strip(), len(), .lower(), .upper(), .split()

text = input('Input a sentence: ')
print(text.strip()) #.strip() removes the extra spaces from a string
print(len(text))
print(text.lower()) #.lower() makes all the characters lower cased
print(text.upper()) #.upper() turns everything into upper cases
print(text.split(',')) #creates a list of items from the string, delimeter is the symbol by which you seperate the strings elements
print(text.capitalize()) #will capitalize
print(text.casefold()) #more aggressive form of text.lower() as in it will even convert the greek letter beta to ss
print(text.count(text[len(text)-1])) #returns the numbr of non-overlapping occurences of substring sub in the range [start,end]

