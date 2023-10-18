num1 = int(input('Pick a number: '))
num2 = int(input('Pick another number: '))

do_what = input('''What do you want to do:
                Add: +
                Sub: -
                Mult: *
                Div: / 
                ''')
if do_what == '+':
    print(num1 + num2)
elif do_what == '-':
    print(num1 - num2)
elif do_what == '*':
    print(num1 * num2)
elif do_what == '/':
    print(num1 / num2)
else:
    print('You didnt pick the right operator!')