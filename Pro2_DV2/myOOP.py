# Testing out what is Object Oriented Program
#    blueprint for car
'''
In Python, the constructor has the name __init()__. 
You also need to pass a special keyword, self, as a 
parameter to the constructor. The keyword self refers 
to the object's instance. Any assignment to this keyword 
means that the attribute ends up on the object instance. 
If you don't add an attribute to self, it will instead 
be treated as a temporary variable that won't exist
 after __init()__ is done executing.

An important takeaway from the code is that __init__() is
 called implicitly. You don't call the __init__() method by name,
  but it's called when the object is created, in this line of code:

  myCar = Car()

'''

class Car(object):

  def __init__(self, model, color, company, speed_limit):
    self.color = color
    self.company = company
    self.speed_limit = speed_limit
    self.model = model

  def start(self):
    print('started')

  def stop(self):
    print('stopped')

  def accelerate(self):
    print('accelerating...')
    # accelerator functionality here'

  def change_gear(self, gear_type):
    print('gear changed')
    # gear related functionality here
