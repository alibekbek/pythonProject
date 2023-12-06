import json


def read_json_file(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            file.close()
        return data
    except FileNotFoundError:
        return None


def update_json_file(file_path, new_d):
    exis_data = read_json_file(file_path) or {}
    exis_data.append(new_d)
    with open(file_path, "w") as file:
        json.dump(exis_data, file)
        file.close()


def add_data_json(file_path):
    print('Enter car')
    car = input()
    print('Enter model')
    mod = input()
    print('Enter V engine')
    v = int(input())
    ex_d = {'name': car, 'model': mod, 'engine': v}
    return ex_d



def delete_json_list(file_path, del_d):
    exis_data = read_json_file(file_path)
    ind = 0
    for i in exis_data:
        if i == del_d:
            exis_data.pop(ind)
            break
        ind += 1

    with open(file_path, "w") as file:
        json.dump(exis_data, file)
        file.close()


