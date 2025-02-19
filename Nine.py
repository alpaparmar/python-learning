# del keyword

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


# s = Student("Jay", 23)
# print(s.name, s.age, "Result of Student Object")

# del s

# print(s)

# Private attributes and methods in Python


class Account:
    def __init__(self, account, password):
        self.account = account
        self.__password = password

    def displayPassword(self):
        return self.__password


a = Account("Jay", "1234")

print(a.displayPassword())

# print(a.__password)


# conceptual implemenations in Python

class Person:

    __name = "Jay"

    def __display(self):
        print("Hello, Worsldldldlld!")

    def welcome(self):
        print("Welcome to Python", self.__display())

p1 = Person()

p1.welcome()


# Inheritance in Python

class Parent:
    def __init__(self):
        print("This is Parent Class")

    @staticmethod
    def display():
        print("This is Parent Class Method")

class Child(Parent):
    def __init__(self):
        print("This is Child Class")

    def display1(self):
        print("This is Child Class Method")

c = Child()

print(c.display())


# Inheritance Types in Python

# Single Inheritance

# Multilevel Inheritance

# Multiple Inheritance


# Super() method in Python

class Car:

    def __init__(self, Type):
        self.Type = Type

    @staticmethod
    def start():
        print("This is Car Started")

    @staticmethod
    def stop():
        print("This is Car Stopped")

class BMW(Car):

    def __init__(self, brand, type):
        self.brand = brand
        super().__init__(type)

car1 = BMW("BMW", "SUV")

print(car1.Type)


# class method

class Person:

    name = "anonymous"

    # def changeName(self, name):
    #     # Person.name = name
    #     self.__class__.name = name

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()

p1.changeName("Jay")
print(p1.name)
print(Person.name)

#Property Decorator

class Student:

    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
    
    @property
    def calculatePercentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"


stu = Student(98, 89, 90)
print(stu.calculatePercentage)

stu.phy = 100

print(stu.calculatePercentage)


# Polymorphism: (Operator Overloading) in Python

print(1 + 2)
print("Hello" + "World")
print([1,2,3] + [4,5,6])


# Complex Number

#exmple ->>> 5i + 3j

# Operator and Dunder Functions

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img, "j")

    def add(self, num2):
        return Complex(self.real + num2.real, self.img + num2.img)


num1 = Complex(5, 3)
print(num1.showNumber())

num2 = Complex(3, 2)
print(num2.showNumber())

print((num1.add(num2)).showNumber())

# Using Dunder Methods

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, num2):
        return Complex(self.real + num2.real, self.img + num2.img)


num1 = Complex(5, 3)
print(num1.showNumber())

num2 = Complex(3, 2)
print(num2.showNumber())

print((num1 + num2).showNumber())


# Here is all the Dunder methods in Python

# __init__ : Constructor
# __del__ : Destructor
# __str__ : String Representation
# __repr__ : Object Representation
# __add__ : Addition
# __sub__ : Subtraction
# __mul__ : Multiplication
# __truediv__ : Division
# __floordiv__ : Floor Division
# __mod__ : Modulus
# __pow__ : Power
# __and__ : Bitwise AND
# __or__ : Bitwise OR
# __xor__ : Bitwise XOR
# __invert__ : Bitwise NOT
# __lshift__ : Left Shift
# __rshift__ : Right Shift
# __eq__ : Equal to
# __ne__ : Not Equal to
# __lt__ : Less than
# __gt__ : Greater than
# __le__ : Less than or Equal to
# __ge__ : Greater than or Equal to
# __contains__ : Check if contains
# __len__ : Length of the object
# __getitem__ : Get item by index
# __setitem__ : Set item by index
# __delitem__ : Delete item by index
# __iter__ : Iterator
# __next__ : Next Element
# __call__ : Call a method
# __getattr__ : Get attribute
# __setattr__ : Set attribute
# __delattr__ : Delete attribute
# __getattribute__ : Get attribute
# __setattr__ : Set attribute
# __delattr__ : Delete attribute
# __getattribute__ : Get attribute
# __setattr__ : Set attribute
# ....So On....