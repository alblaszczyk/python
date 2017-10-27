class Shape(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def calculate_area(self):
        return self.x * self.y

my_shape = Shape(40, 60)
print(my_shape)
print(my_shape.calculate_area())
