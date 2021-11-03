# This is to protect data for calling while manipulating it
# methods can carry out an action. That action can be a computation 
# that only relies on inputs, or it can change the value of a variable.
# refer to Build real world applications with Python Introduction to object-oriented programming 
# with Python Add behavior with methods <<Unit 5 of 9>>

class Square:
    def __init__(self):
      self.__height = 2
      self.__width = 2
    def set_side(self, new_side):
      self.__height = new_side
      self.__width = new_side

square = Square()
square.__height = 9 # raises AttributeError
square.__height = 6 # raises AttributeError
square._height = 9 # raises AttributeError
print(square._height)
square._height = 6 # raises AttributeError
print(square._height)
print(square.__height)
square._Square__height = 3 # is allowed
print(square.__height)

