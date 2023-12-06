class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        s = [f'{x.name}: {x.price}' for x in self.goods]
        return s


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()
cart.add(TV('Samsung', 1000))
cart.add(TV('LG', 1500))
cart.add(Table('IKEA', 200))
cart.add(Notebook('Asus', 500))
cart.add(Notebook('Acer', 400))
cart.add(Cup('II', 10))
print(cart.get_list())


