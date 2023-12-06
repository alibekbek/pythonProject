login_data = {'user': {'password': '123456'}, 'user2': {'password': '987654'}}          # Словарь из логинов-паролей


def check_un_ps(u, p):      # Функция проверки логинов-паролей
    if u not in login_data:     # Проверка на отсутствие логина в словаре
        print('Sorry username is incorrect')
    else:
        if login_data[u]['password'] == p:      # Проверка на правильность пароля
            print('You\'re logged in')
            while True:
                print('Do you want to log out? \n 1) Yes \n 2) No ')
                lf = input()
                if lf == '1':
                    print('Bye-bye')
                    return False
                else:
                    print('You are still here')

        else:
            print(f'Sorry, password for \'{u}\' is incorrect')


def create_new_acc():       # Функция по созданию нового логина-пароля
    print('Enter Username: ')
    u = input()
    if u not in login_data:             # Проверка на отсутствие логина
        print('Enter your password: ')
        p = input()
        login_data.setdefault(u, {'password': p})       # Заносим в словарь логин: пароль
        print('New account created!')
    else:
        print(f'Sorry, username \'{u}\' is registered yet. Please try again.')  # Если логин уже существует
        print(' 1) Try again \n 2) Exit')
        s = input()
        if s == '1':
            create_new_acc()    # Рекурсия, пока не введется уникальный логин
        else:
            exit()


while True:
    print('Do you have any account? \n 1) Yes \n 2) No \n 3) Exit')
    start = input()
    if start == '1':
        print('Enter your username please ')
        un = input()                        # Вводим логин
        print('Enter your password: ')
        ps = input()                        # Вводим пароль
        check_un_ps(un, ps)                 # Проверяем правильность

    elif start == '2':
        print('Do you want to create new account? \n 1) Yes \n 2) No')
        v = input()
        if v == '1':                        # Создаем новый логин
            create_new_acc()
        else:
            break
    else:
        break
