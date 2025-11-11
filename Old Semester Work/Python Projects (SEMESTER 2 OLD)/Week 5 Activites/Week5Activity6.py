class Circle:
    def __init__(self, radius):
        self._radius = radius
    def rad(self):
        return self._radius

c = Circle(10)

print(c.rad())
