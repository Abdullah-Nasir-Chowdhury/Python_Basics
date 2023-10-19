#functions:
def addTwo(x):
    return x + 2

print(addTwo(2))
new_number = addTwo(2)
print(new_number)

def sum_numbers(*args):
    print(sum(args))

def sum_numbers_2(*args):
    total = 0
    for arg in args:
        total += arg
    print(total)

sum_numbers(2,2,2,2,2)
sum_numbers_2(2,2,2,2,2,2)