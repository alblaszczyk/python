class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg
  def display_car(self):
    print "This is a %s %s with %s MPG." % (self.color, self.model, self.mpg)
  def drive_car(self):
    self.condition = "used"
class ElectricCar(Car):
  def __init__(self, model, color, mpg, battery_type):
    self.model = model
    self.color = color
    self.mpg   = mpg
    self.battery_type = battery_type

my_car1 = Car("DeLorean", "silver", 88)

print my_car1.condition
my_car1.drive_car()
print my_car1.condition

my_car = ElectricCar("Dodge", "black", 66, "molten salt")