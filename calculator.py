while True:
    number1 = input('Please, Enter the first number:')
    number2 = input('Enter the second of number:')
    choice = input('Select the operation + or - 5: ')
    if choice == '+':
        print(int(number1) + int(number2))
    else:
        print(int(number1) - int(number2))