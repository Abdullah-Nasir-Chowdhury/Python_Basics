file = open('ReadMeBro.txt', 'r') # opens the files, reads it because 'r'
f = file.readlines()
print(f)

# remove all the \n i.e carriage returns:
newList = []
for line in f:
    if line[-1] == '\n':
        newList.append(line[:-1])
    else:
        newList.append(line)

print(newList)


# easier method:
newList2 = []
for line in f:
    newList2.append(line.strip())
print(newList2)