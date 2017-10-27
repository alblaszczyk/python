class Animal(object):
  """Makes cute animals."""
  is_alive = True
  health = "good"
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def description(self):
    print self.name
    print self.age

hippo = Animal("POTEZNY", 3)
sloth = Animal("Lazy", 12)
ocelot = Animal("Kitty", 4)
hippo.description()
print hippo.health
print ocelot.health
print sloth.health
