import json


class System:
    def __init__(self):
        self.d2 = self.read_json_file("data_user.json")
        self.d = []                                         # Users Database

    def login_user(self, username, password):
        if username in self.d2 and self.d2[username]["password"] == password:
            print(f'Welcome, {username}')
            self.d2[username]["isLogin"] = True
            self.update_json_file("data_user.json", self.d2)
        else:
            print('Username or password is incorrect')

    def add_user(self, username, password, user_type):
        match user_type:
            case "Teacher":
                self.d.append(Teacher(username, password))
            case "Student":
                self.d.append(Student(username, password))
            case _:
                return
        self.d2.setdefault(username, {"username": username,
                                      "password": password,
                                      "type": user_type,
                                      "isAdmin": False,
                                      "isLogin": False})
        self.update_json_file("data_user.json", self.d2)

    @staticmethod
    def read_json_file(file_path):  # Функция для считывания файла
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
                file.close()
            return data
        except FileNotFoundError:
            return None

    @staticmethod
    def update_json_file(file_path, new_d):  # Функция для обновления файла
        with open(file_path, "w") as file:
            json.dump(new_d, file, indent=5)
            file.close()


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    d = System.read_json_file("data_user.json")
    

class Admin(User):
    @staticmethod
    def delete_user(username):
        User.d.pop(username)
        System.update_json_file("data_user.json", User.d)


class Teacher(User):
    @staticmethod
    def delete_user(username):
        User.d.pop(username)
        System.update_json_file("data_user.json", User.d)


class Student(User):
    pass


Admin.delete_user("John")