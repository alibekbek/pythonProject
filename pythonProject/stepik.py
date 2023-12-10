class LineTo:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PathLines:
    def __init__(self, *args):
        self.coords = list((LineTo(0, 0), ) + args)

    def get_path(self):
        return self.coords[1:]

    def get_length(self):
        res = 0
        if len(self.coords) == 1:
            return res
        elif len(self.coords) == 2:
            res = (self.coords[1].x ** 2 + self.coords[1].y ** 2) ** 0.5
        for i in range(1, len(self.coords)):
            res += ((self.coords[i].x - self.coords[i-1].x) ** 2 + (self.coords[i].y - self.coords[i-1].y) ** 2) ** 0.5
        return res

    def add_line(self, line):
        self.coords.append(line)


p = PathLines(LineTo(10, 0), LineTo(20, 0))
#p = PathLines()
p.add_line(LineTo(30, 0))
#dist = p.get_length()
print(p.get_path())
print(p.get_length())

