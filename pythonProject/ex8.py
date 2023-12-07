class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, text):
        self.__data = text

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, o):
        if isinstance(o, StackObj) or o is None:
            self.__next = o


class Stack:
    def __init__(self):
        self.top = None
        self.last = None

    def push(self, obj: StackObj):
        if self.last:
            self.last.next = obj
        self.last = obj
        if self.top is None:
            self.top = obj

    def pop(self):
        i = self.top
        if not i:
            return
        while i and i.next != self.last:
            i = i.next
        if i:
            i.next = None
        last = self.last
        self.last = i
        if self.last is None:
            self.top = None
        return last

    def get_data(self):
        lst = []
        i = self.top
        while i:
            lst.append(i.data)
            i = i.next
        return lst
