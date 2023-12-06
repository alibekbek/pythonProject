def check_all_grades(x):                    # Функция вывода всех оценок
    print(f'Points by MATH:')
    for i in x["math"]:
        print(f'{i} - {x["math"].get(i)}')

    print(f'Points by ENGLISH:')
    for i in x["english"]:
        print(f'{i} - {x["english"].get(i)}')


def change_exam_points(x):                  # Функция редактирования оценок
    print('What subject?\n 1) Math\n 2) English')
    sub = int(input())
    print('Which Student?')
    sub1 = "math" if sub == 1 else "english"
    print(*x[sub1].keys())
    st = input()
    print('Enter new Grade: ')
    p = int(input())
    try:
        x[sub1][st] = p
    except:
        x[sub1].setdafault(st, p)           # Если будет введен логин несуществующего в списке студента
    print(f'Now {st} has a {p} points by {sub1}')
    return x


def monitoring(x: dict):                    # Функция для просмотра мониторинга успеваемости студентов
    s1 = [i for i in x["math"] if x["math"].get(i) >= 50]
    s2 = [i for i in x["math"] if x["math"].get(i) < 50]
    print(f'Pass students by MATH')
    print(*s1)
    print(f'Fail students by MATH')
    print(*s2)
    s3 = [i for i in x["english"] if x["english"].get(i) >= 50]
    s4 = [i for i in x["english"] if x["english"].get(i) < 50]
    print(f'Pass students by ENGLISH')
    print(*s3)
    print(f'Fail students by ENGLISH')
    print(*s4)
