m, d = map(int, input().split())
ta = [1, 3, 5, 7, 8, 10, 12]
tr = [4, 6, 9, 11]
dv = [2]
if m in ta:
    if d == 31:
        print(f'{str(m).rjust(2, "0")}.{str(d-1).rjust(2, "0")} {str(m+1).rjust(2, "0")}.01')
    elif m == 8 and d == 1:
        print('07.31 08.02')
    elif m == 1 and d == 1:
        print('12.31 01.02')
    elif d == 1:
        print(f'{str(m-1).rjust(2, "0")}.30 {str(m).rjust(2, "0")}.02')
    else:
        print(f'{str(m).rjust(2,"0")}.{str(d-1).rjust(2,"0")} {str(m).rjust(2,"0")}.{str(d+1).rjust(2,"0")}')
elif m in tr:
    if d == 30:
        print(f'{str(m).rjust(2, "0")}.{str(d-1).rjust(2,"0")} {str(m+1).rjust(2, "0")}.01')
    elif d == 1:
        print(f'{str(m-1).rjust(2, "0")}.31 {str(m).rjust(2,"0")}.{str(d+1).rjust(2,"0")}')
    else:
        print(f'{str(m).rjust(2, "0")}.{str(d - 1).rjust(2, "0")} {str(m).rjust(2, "0")}.{str(d + 1).rjust(2, "0")}')

elif m in dv:
    if d == 28:
        print(f'{str(m).rjust(2, "0")}.{str(d-1).rjust(2, "0")} 03.01')
