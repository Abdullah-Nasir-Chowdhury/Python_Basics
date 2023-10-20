var = 9
loop = True

def func(x):
    newVar = 7
    var = 10
    if x == 5:
        return newVar, var

# print(newVar)
# this will give error because newVar is a local variable to function func
# whereas, var and loop are global variables.
print(var)