import sys

# программу не менять, только добавить два метода
lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):
        self.a = [i.split() for i in data]
        self.ls = []
        for i in range(len(self.a)):
            self.d = {self.FIELDS[x]: self.a[i][x] for x in range(len(self.FIELDS))}
            self.ls.append(self.d)

        return self.ls

    def select(self, a, b):

        if b > len(self.ls):
            b = len(self.ls)-1
        self.ls2 = []
        i = a
        while i <= b:
            self.ls2.append(self.ls[i])
            i += 1
        return print(self.ls2)


db = DataBase()
db.insert(lst_in)