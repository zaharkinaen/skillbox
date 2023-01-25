while True:
    num1 = int(input('Введите 1 число: '))
    num2 = int(input('Введите 2 число: '))
    do = input('Введите действие: ')
    if do == '+':
        print(num1, '+', num2, '=', num1 + num2)
    elif do == '-':
        print(num1, '-', num2, '=', num1 - num2)
    elif do == '*':
        print(num1, '*', num2, '=', num1 * num2)
    elif do == '/':
        print(num1, '/', num2, '=', num1 / num2)
    else:
        print('Ошибка: такой операции не существует. Попробуйте ещё раз.')
