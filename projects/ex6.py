dob = input('what is your age?')
current_year = 2023

while int(dob) <= int(current_year):
    client_age = int(current_year)-int(dob)
    print(client_age)
    if client_age < 0:
        print('OMG your age is negative please enter again!')
    dob = input('what is your age?')
    if int(dob) == 0:
        break
