class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def plus(self):
        return self.x + self.y

    def minus(self):
        return self.x - self.y

    def umnozh(self):
        return self.x * self.y

    def delen(self):
        if self.y == 0:
            raise ValueError('Na nol delit nelzya')
        else:
            return self.x / self.y

    def sqrt(self):
        if self.x < 0:
            raise ValueError('Net kornya ot otricatelnogo')
        else:
            return self.x ** 0.5

    def power(self):
        return self.x ** self.y
