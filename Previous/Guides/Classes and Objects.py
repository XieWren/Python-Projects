class Vehicle:
    
  def __init__(self, name, kind, colour, value): #Without __init__, variables of the various objects
    self.name = name                             #(e.g.car2.name) will be unable to be called
    self.kind = kind
    self.colour = colour
    self.value = value 

  def description(self):
    print("{} is a {} {} worth ${}".format(self.name, self.colour, self.kind, self.value))

#Use the Vehicle class to create an object "car", and then execute the "description" method:

car1 = Vehicle("Fer","convertible","red","60000.00")
car2 = Vehicle("Jump","van","blue","10000.00")

car1.description()                                              #   Deleting object properties:
car2.description()                                              #   del car1.name

car2.kind="jeep"    #Modifying object properties                #   Deleting objects:
car2.description()                                              #   del car1

#Class Inheritance
class Empty(Vehicle):       #<-- Properties and methods of "Vehicle" class also inherited
#   pass                     <-- Definitions cannot be empty, so put "pass" when empty to avoid error
    def __init__(self, name, variable):
        Vehicle.__init__(self, name)        #__init__() overrides inheritance, thus has to be re-added.
                                            #super().__init__() also works, without needing to specify class again.
        
        self.variable="variable" #Adding more variables. Note the parameters in the first __init__(). Methods can also be added.
"""
Alternatively:
‾‾‾‾‾‾‾‾‾‾‾‾‾‾
class Vehicle:
  def description(self, name, kind, colour, value):
    print("{} is a {} {} worth ${}".format(name, colour, kind, value))

car1 = Vehicle()
car2 = Vehicle()

car1.description("Fer","convertible","red","60000.00")         #Without __init__, parameters of functions have
car2.description("Jump","van","blue","10000.00")               #to be entered the way they usually are.

"""

"""
Glossary
‾‾‾‾‾‾‾‾
┌────────────────────────────────────────────────────────────────────────────────────────────────────┐
│Method:           Methods in objects are functions that belong to the object.                       │
├────────────────────────────────────────────────────────────────────────────────────────────────────┤
│__init__:         A function all classes have, which is always executed when the class is initiated.│
│                  Used to assign values to object properties, or for operations necessary for the   │
│                  object to be created.                                                             │
├────────────────────────────────────────────────────────────────────────────────────────────────────┤
│object:           An instance of a class, with a specific set of variables                          │
├────────────────────────────────────────────────────────────────────────────────────────────────────┤
│class:            An object constructor, or a "blueprint" for creating objects using specific       │
│                  variables and functions                                                           │
├────────────────────────────────────────────────────────────────────────────────────────────────────┤
│self:             A parameter referring to the current instance of the class, used to access        │
│                  variables that belongs to the class. It does not have to be named self, but it has│
│                  to be the first parameter of any function in the class                            │
└────────────────────────────────────────────────────────────────────────────────────────────────────┘  
"""

"""
Acknowledgements
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
1)https://www.learnpython.org/en/Classes_and_Objects
2)https://www.w3schools.com/python/python_classes.asp
3)https://www.w3schools.com/python/python_inheritance.asp
""" 
