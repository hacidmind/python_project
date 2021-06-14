num1 = int(input('num1: '))
op = input('operators: ')
num2 = int(input('num2: '))

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1 * num2)
elif op == '/':
    print(num1 / num2)
else:
    print('Invalid operator')
