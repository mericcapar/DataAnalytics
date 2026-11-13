code = int(input("Enter your department code: "))
match code:
    case 1:
        print('Marketing')
    case 5:
        print('Human Resources')
    case 10:
        print('Accounting')
    case 12:
        print('Legal')
    case 18:
        print('IT')
    case 20:
        print('Customer Relations')
    case _:
        print('Enter a valid code.')

    #I believe if else is more understable than match case. It is also more common than match case.
    