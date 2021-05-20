# Classes
""" Object-oriented programming is one of the most effective approaches to writing software. In object-oriented programming you write classes that represent real-world things and situations, and you create objects based on these classes. When you write a class, you define the general behavior that a whole category of objects can have. 
When you create individual objects from the class, each object is automatically equipped with the general behavior; you can then give each object whatever unique traits you desire. You’ll be amazed how well real-world situations can be modeled with object-oriented programming.Making an object from a class is called instantiation, and you work with instances of a class """

# Creating and Using a Class
""" class, Dog, that represents a dog—not one dog in particular, but any dog. What do we know about most pet dogs? Well, they all have a name and age. We also know that most dogs sit and roll over. Those two pieces of information (name and age) and those two behaviors (sit and roll over) will go in our Dog class because they’re common to most dogs. This class will tell Python how to make an object representing a dog. After our class is written, we’ll use it to make individual instances, each of which represents one specific dog """
"""  By convention, capitalized names refer to classes in Python. There are no parentheses in the class definition because we’re creating this class from scratch """
class Dog:
    # A simple attempt to model a dog.
    
    """ A function that’s part of a class is a method. Everything you learned about functions applies to methods as well. """
    """ The __init__() method is a special method that Python runs automatically whenever we create a new instance based on the Dog class. This method has two leading underscores and two trailing underscores, a convention that helps prevent Python’s default method names from conflicting with your method names. The self parameter is required in the method definition, and it must come first before the other parameters. Every method call associated with an instance automatically passes self, which is a reference to the instance itself; it gives the individual instance access to the attributes and methods in the class """
    def __init__(self, name, age):
        # Initialize name and age attributes.
        self.name = name
        self.age = age
 
    def sit(self):
        # Simulate a dog sitting in response to a command.
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        # Simulate rolling over in response to a command.
        print(f"{self.name} rolled over!")

# Making an Instance from a Class
""" Think of a class as a set of instructions for how to make an instance. The class Dog is a set of instructions that tells Python how to make individual instances representing specific dogs """
""" The naming convention is helpful here: we can usually assume that a capitalized name like Dog
refers to a class, and a lowercase name like my_dog refers to a single instance created from a class """
""" my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.") """

# Accessing Attributes --> To access the attributes of an instance, you use dot notation

# Calling Methods --> After we create an instance from the class Dog, we can use dot notation to call any method defined in Dog
""" my_dog.sit()
my_dog.roll_over() """

# Creating Multiple Instances --> You can create as many instances from a class as you need
""" my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit() """

# Working with Classes and Instances
""" class Car:
    def __init__(self, make, model, year):
        # Initialize attributes to describe a car.
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 100 # Setting a Default Value for an Attribute, not mandatory
    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        # Modifying an Attribute’s Value Through a Method
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        # Incrementing an Attribute’s Value Through a Method
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("This car need a gas tank!") """
 
""" my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.odometer_reading = 23 # Modifying an Attribute’s Value Directly
my_new_car.read_odometer()

my_new_car.update_odometer(25) # Modifying an Attribute’s Value Through a Method
my_new_car.read_odometer()

# Incrementing an Attribute’s Value Through a Method
my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23_500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer() """

""" You can use methods like this to control how users of your program update values such as an odometer reading, but anyone with access to the program can set the odometer reading to any value by accessing the attribute directly. Effective security takes extreme attention to detail in addition to basic checks like those shown here """

####################################################################################################

# Inheritance
""" You don’t always have to start from scratch when writing a class. If the class you’re writing is a specialized version of another class you wrote, you can use inheritance. When one class inherits from another, it takes on the attributes and methods of the first class. The original class is called the parent class, and the new class is the child class. The child class can inherit any or all of the attributes and methods of its parent class, but it’s also free to define new attributes and methods of its own """

# The __init__() Method for a Child Class
""" When you’re writing a new class based on an existing class, you’ll often want to call the __init__() method from the parent class. This will initialize any attributes that were defined in the parent __init__() method and make them available in the child class. """

""" class ElectricCar(Car):
    # The name of the parent class must be included in parentheses in the definition of a child class

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 75 # Defining Attributes for the Child Class
        # The super() function at x is a special function that allows you to call a method from the parent class. This line tells Python to call the __init__() method from Car, which gives an ElectricCar instance all the attributes defined in that method. The name super comes from a convention of calling the parent class a superclass and the child class a subclass
    
    def describe_battery(self):
        # Defining Methods for the Child Class
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")
        # Overriding Methods from the Parent Class. You can override any method from the parent class that doesn’t fit what you’re trying to model with the child class. To do this, you define a method in the child class with the same name as the method you want to override in the parent class. Python will disregard the parent class method and only pay attention to the method you define in the child class


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank() """

# Instances as Attributes
""" When modeling something from the real world in code, you may find that you’re adding more and more detail to a class. You’ll find that you have a growing list of attributes and methods and that your files are becoming lengthy. In these situations, you might recognize that part of one class can be written as a separate class. You can break your large class into smaller classes that work together """

""" class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 100  
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles
    def fill_gas_tank(self):
        print("This car need a gas tank!")

class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range() """


# Importing Classes
""" from car import Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer() """

# Importing Multiple Classes from a Module
""" from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name()) """

# Importing an Entire Module
""" import car
my_beetle = car.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())
my_tesla = car.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name()) """

# Importing All Classes from a Module
""" from car import * 
my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name()) """

# Using Aliases
""" from car import ElectricCar as EC
my_tesla = EC('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name()) """

# The Python Standard Library
""" from random import randint, choice

print(randint(1, 6))
players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)
print(first_up) """

