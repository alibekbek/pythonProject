import json


def read_json_file(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            file.close()
        return data
    except FileNotFoundError:
        return None


def delete_json_list(file_path, delete_data):
    existing_data = read_json_file(file_path)
    ind = 0
    for i in existing_data["user"]:
        if i['username'] == delete_data:
            existing_data["user"].pop(ind)
            break
        ind += 1
    print(existing_data["user"])
    with open(file_path, "w") as file:
        json.dump(existing_data, file, indent=4)
        file.close()


def update_json_file(file_path, new_d):
    existing_data = read_json_file(file_path) or {"user": []}
    existing_data["user"].append(new_d)

    with open(file_path, "w") as file:
        json.dump(existing_data, file, indent=4)
        file.close()


def new_user():
    print('Enter username')
    un = input()
    print('Enter password:')
    ps = input()
    print('Your gender? M / F')
    g = input()
    data_form = {"username": un, "password": ps, "gender": g, "isLogin": False}
    return data_form


#new_data = new_user()

#update_json_file("user.json", new_data)

delete_json_list("user.json", 'aaa')