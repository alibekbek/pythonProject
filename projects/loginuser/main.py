import json
import random           # Random для выбора случайного Учителя и Студента
import teacher
import re


m = 'MATH'              # Текстовые названия предметов
E = 'ENGLISH'


def action_choice():                        # Основная фунция логин-реджистер
    print('Hello! Please choice your action: \n 1) Login user\n 2) Register new user\n 3) Exit')
    r = input()
    match r:                                # Функция match для выбора без if elif else
        case '1':
            print('Login')
            login_user()                    # Запуск функции для входа в систему
        case '2':
            print('Register new user')
            create_new_acc(0)                # Запуск функции для добавления нового юзера
        case '3':
            exit()                          # Выход из программы
        case _:
            action_choice()


def login_user():                           # Функция логина
    print('Enter you username: ')           # Вводим логин
    name = input()
    print('Enter your password: ')          # Вводим пароль
    password = input()

    if name in db and db[name]["password"] == password:             # Проверяем на наличие логина и корректность пароля
        if db[name]["type"] == "admin":
            print(f'Welcome, {name}!')
            db[name]["isLogin"] = True
            update_json_file("data2.json", db)
            admin_act(name)                                             # Запуск функций для Админа
        elif db[name]["type"] == "Teacher":
            print(f'Welcome, Teacher {name}')
            db[name]["isLogin"] = True
            update_json_file("data2.json", db)
            choice_act_teach(name)                                  # Запуск функций для Учителя
        elif db[name]["type"] == "Student":
            print(f'Welcome, Student {name}')
            db[name]["isLogin"] = True
            update_json_file("data2.json", db)
            choice_act_st(name)                                     # Запуск функций для Студента

    else:
        print("Please check your username and password")            # Повторно запрашиваем логин-пароль
        login_user()


def create_new_acc(t):       # Функция по созданию нового логина-пароля, если t = 1, то админ, если 0, то обычный
    print('Enter Username: ')
    u = input()
    if u not in db:             # Проверка на отсутствие логина
        p = new_psw()
        if t == 0:
            print('Enter your role: \n 1) Teacher\n 2) Student')
            r = int(input())
        elif t == 1:
            print('Your role is Admin')
        print('Enter your name:')
        name = input()
        print('Enter your surname:')
        surname = input()
        print('Enter your age:')
        age = input()
        if t == 0:
            db.setdefault(u, {'username': u,
                              'password': p,
                              'type': "Teacher" if r == 1 else "Student",
                              'name': name,
                              'surname': surname,
                              'age': int(age),
                              'isAdmin': False,
                              'isLogin': False})       # Заносим в словарь
        elif t == 1:
            db.setdefault(u, {'username': u,
                              'password': p,
                              'type': "admin",
                              'name': name,
                              'surname': surname,
                              'age': int(age),
                              'isAdmin': True,
                              'isLogin': False})
        update_json_file("data2.json", db)
        print('New account created!')
    else:
        print(f'Sorry, username \'{u}\' is registered yet. Please try again.')  # Если логин уже существует
        print(' 1) Try again \n 2) Exit')
        s = input()
        if s == '1':
            create_new_acc(t)    # Рекурсия, пока не введется уникальный логин
        else:
            action_choice()


def read_json_file(file_path):          # Функция для считывания файла
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            file.close()
        return data
    except FileNotFoundError:
        return None


def update_json_file(file_path, new_d):     # Функция для обновления файла
    with open(file_path, "w") as file:
        json.dump(new_d, file, indent=8)
        file.close()


db = read_json_file("data2.json")           # Считываем файл с username


def admin_act(n):                        # Функции для Админа
    print('Your status is Admin. Select your action')
    print(' 1) Change user\'s status\n 2) Change user\'s role (Teacher/Student)\n 3) Change user\'s info\n'
          ' 4) Functions of Teacher\n 5) Functions of Student\n 6) Register new Admin-user\n 7) Logout')
    a = input()
    match a:
        case '1':                       # Изменить статус Админ-неАдмин
            print('Change user\'s status')
            change_status()
            admin_act(n)
        case '2':                       # Изменить роль Учитель-Студент
            print('Change user\'s role')
            change_role()
            admin_act(n)
        case '3':                       # Изменить информацию по пользователю
            print('Change user\'s info')
            change_info()
            admin_act(n)
        case '4':
            print('Functions of Teacher')   # Использование функций учителя
            teach = [i for i in db if db[i]["type"] == "Teacher"]       # Выбираем случайный логин среди учителей
            db[n]["isLogin"] = False
            update_json_file("data2.json", db)
            choice_act_teach(random.choice(teach))
        case '5':
            print('Functions of Student')       # Использование функций студентов
            stud = [i for i in db if db[i]["type"] == "Student"]        # Выбираем случайный логин среди студентов
            db[n]["isLogin"] = False
            update_json_file("data2.json", db)
            choice_act_st(random.choice(stud))
        case '6':
            print('Registering new Admin-user')
            create_new_acc(1)
            admin_act(n)
        case '7':
            print('Logout')
            db[n]["isLogin"] = False
            update_json_file("data2.json", db)
            action_choice()


def change_status():                    # Функция для изменения статуса Админа, кроме самого admin
    print('List of usernames: ')
    for i in db:
        if i == "admin":
            continue
        else:
            print(f'{i} - ', 'Admin' if db[i]['isAdmin'] else 'NotAdmin')
    print('Enter username:')
    name = input()
    if name in db:
        db[name]['isAdmin'] = False if db[name]['isAdmin'] else True
        print(f'You\'re changed status of {name} to status:')
        print('Admin' if db[name]['isAdmin'] else 'NotAdmin')
        update_json_file("data2.json", db)              # Обновляем json-файл
    else:
        change_status()


def change_role():                  # Функция для изменения роли Учитель-Студент, обходя admin
    print('List of usernames: ')

    for i in db:
        if db[i]['type'] == 'admin':
            continue
        else:
            print(f'{i} - ', 'Teacher' if db[i]['type'] == 'Teacher' else 'Student')
    print('Enter username:')
    name = input()
    if name in db:
        db[name]["type"] = "Teacher" if db[name]["type"] == "Student" else "Student"
        print(f'You\'re changed role of {name} to :')
        print('Teacher' if db[name]["type"] == "Teacher" else "Student")
        update_json_file("data2.json", db)              # Обновляем json-файл
    else:
        change_role()


def change_info():
    print('User\'s info changing. Choice username please: ')
    print(*[i for i in db])                     # Выбираем пользователя
    name = input()
    if name in db:
        print('Select parameter')               # Выбираем параметр для изменения
        for i, keys in enumerate(db[name]):
            print((i+1), keys)
        parameter = int(input())-1
        match parameter:
            case 0:                         # Изменение логина и автоматически создание новой ветки в dict
                print('Input new username: ')
                un = input()
                db[name]["username"] = un
                db.setdefault(un, {"username": un,
                                   "password": db[name]["password"],
                                   "type": db[name]["type"],
                                   "name": db[name]["name"],
                                   "surname": db[name]["surname"],
                                   "age": db[name]["age"],
                                   "isAdmin": db[name]["isAdmin"],
                                   "isLogin": False})
                db.pop(name)
            case 1:                         # Изменение пароля
                print('Input new password: ')
                db[name]["password"] = input()
            case 2:                         # Изменение типа учитель-студент
                print('Input new type of user: \n 1) Teacher\n 2) Student')
                t = int(input())
                db[name]["username"] = "Teacher" if t == 1 else "Student"
            case 3:                         # Изменение имени
                print('Input new name: ')
                db[name]["name"] = input()
            case 4:                         # Изменение фамилии
                print('Input new surname: ')
                db[name]["surname"] = input()
            case 5:                         # Изменение возраста
                print('Input new age: ')
                db[name]["age"] = int(input())
            case 6:                         # Изменение статуса Админ
                print('Input status \'isAdmin\': \n 1) True\n 2) False')
                s = int(input())
                db[name]["isAdmin"] = True if s == 1 else False
            case 7:
                print('It is impossible to change parameter isLogin')
            case _:
                print('Going to up menu')
        update_json_file("data2.json", db)


def choice_act_teach(n):            # Выбор действий Учителя
    print(f'{n}, your status is Teacher. Select your action')
    print(' 1) Check all grades\n 2) Change exam points\n 3) Student\'s monitoring\n 4) Logout\n')
    s = input()
    match s:
        case '1':               # Вывод всех оценок
            print('Checking all grades')
            teacher.check_all_grades(marks)
            choice_act_teach(n)
        case '2':               # Редактирование оценок
            print('Change exam points')

            update_json_file("data3.json", teacher.change_exam_points(marks))
            choice_act_teach(n)
        case '3':               # Мониторинг студентов по успеваемости
            print('Student\'s monitoring')
            teacher.monitoring(marks)
            choice_act_teach(n)
        case '4':               # Выход из системы
            print(f'Logout from user {n}')
            db[n]["isLogin"] = False
            update_json_file("data2.json", db)
            action_choice()
    return


marks = read_json_file("data3.json")        # Создаем лист с оценками студентов


def choice_act_st(n):               # Выбор действий студента
    print(f'{n}, your status is Student. Select your action')
    print(' 1) Check your grades\n 4) Logout\n')
    s = input()
    match s:
        case '1':                   # Просмотр оценок
            print('Checking all grades')
            check_st_points(n)
            choice_act_st(n)
        case '4':                   # Выход из системы
            print(f'Logout from user {n}')
            db[n]["isLogin"] = False
            update_json_file("data2.json", db)
            action_choice()
        case _:
            action_choice()
    return


def check_st_points(n):             # Функция формирования оценок студента
    try:
        print(f'You have a grade {marks["math"][n]} for {m}')
        print(f'You have a grade {marks["english"][n]} for {E}')
    except:
        print('There is no grades')


def new_psw():
    print("Enter new password")
    psw = input()
    res = re.findall(r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*]).{8}$', psw)
    p1 = psw
    if len(res) > 0:
        print('Password\'s type is correct')
        return p1
    else:
        print('Password\'s type is incorrect')
        return new_psw()


while True:
    action_choice()
