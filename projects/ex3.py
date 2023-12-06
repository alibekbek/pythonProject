math = {'Madi': 78, 'Josh': 49, 'Bakhytzhan': 100}
english = {'Madi': 65, 'Josh': 100, 'Bakhytzhan': 30}
m = 'MATH'
E = 'ENGLISH'


def choice_less():
    c = input('What the lesson? \n 1) Math\n 2) English\n 3) Exit\n')
    return c


# Выбор действий для Учителя
def choice_act_teach():
    s = input('Select your choice: \n'
              ' 1) Check all grades \n'
              ' 2) Change exam points \n'
              ' 3) Student\'s monitoring \n'
              ' 4) Exit\n')
    return s


# Посмотреть все оценки
def check_all_grades(x: dict, y):
    print(f'Points by {y}')
    print('Grades: ')
    for i in x:
        print(f'{i} - {x[i]}')


# Выбор для Студента
def choice_act_st():
    s = input('Select your choice: \n 1) Check all grades \n'
              '\n 3) Exit\n')
    return s


# Редактирование оценок Учителем
def change_exam_points(x: dict, y):
    print('Which Student?')
    print(*x.keys())
    st = input()
    print('Enter new Grade: ')
    p = int(input())
    x[st] = p
    print(f'Now {st} has a {p} points by {y}')


def check_st_points(s, x: dict, y):
    print(f'{s} has a grade {x[s]} for {y}')


# Разделение на группы студентов (PASS / FAIL)
def monitoring(x: dict, y):

    s1 = [i for i in x if x[i] >= 50]
    s2 = [i for i in x if x[i] < 50]
    print(f'Pass students by {y}')
    print(*s1)
    print(f'Fail students by {y}')
    print(*s2)


def teach_acts():

    return


while True:

    r = input('What\'s your role: \n 1) Teacher; \n 2) Student \n 3) Exit\n')

    if r == '1':                            # Роль Учителя

        a = choice_less()                   # Выбираем урок
        if a == '1':                        # Математика
            a1 = choice_act_teach()         # Выбираем действие

            if a1 == '1':                   # Просмотр оценок
                check_all_grades(math, m)
            elif a1 == '2':                 # Редактирование оценов
                change_exam_points(math, m)
            elif a1 == '3':
                monitoring(math, m)         # Разделение на группы студентов по успеваемости
            else:
                break

        elif a == '2':                      # Английский
            a1 = choice_act_teach()
            if a1 == '1':                   # Просмотр оценок
                check_all_grades(english, E)
            elif a1 == '2':                 # Редактирование оценов
                change_exam_points(english, E)
            elif a1 == '3':
                monitoring(english, E)      # Разделение на группы студентов по успеваемости
            else:
                break

    elif r == '2':                          # Роль Студента
        a = choice_less()                   # Выбираем урок
        if a == '1':                        # Математика
            a1 = choice_act_st()            # Выбираем действие
            if a1 == '1':                   # Просмотр оценок
                print('Enter your name: ')
                n = input()
                check_st_points(n, math, m)

            else:
                break

        elif a == '2':                      # Английский
            a1 = choice_act_st()
            if a1 == '1':  # Просмотр оценок
                print('Enter your name: ')
                n = input()
                check_st_points(n, english, E)
            else:
                break
    else:                                   # Общий выход из программы
        break
