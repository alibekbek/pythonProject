class User:
    def __init__(self, name, surname, username):
        self.name = name
        self.surname = surname
        self.username = username

    def get_email(self):
        return f'{self.name}.{self.surname}@gmail.com'

    def get_info(self):
        return f'{self.name} {self.surname} : {self.get_email()} ; {self.username}'

