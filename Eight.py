#OOPS in Python

#OOP in Python

# Class & Object in Python


# Creating Class

class Person:
    name = "Jay Parmar"


# Creating Object
    
p = Person()
print(p.name, "Result of Onject")

class Car:
    name = "BMW"
    model = "2020"
    color = "Black"

c = Car()
print(c.name, c.model, c.color, "Result of Car Object")


# __init__ method in Python

#Constructor in Python

class NewPerson:

    #default constructor
    def __init__(self):
        print("This is default constructor")

    #parameterized constructor
    def __init__(self, name):
        self.name = name

newP = NewPerson("JPJP")
print(newP.name, "Result of NewPerson Object")


# Class and Instance Attributes in Python

class Student:
    name = "Jay"
    age = 23

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self, name, age):
        self.extName = name
        self.extAge = age
        print("Name:", self.extName)
        print("Age:", self.extAge)

s = Student("JP", 23)
print(s.name, s.age, "Result of Student Object")
print(Student.name, Student.age, "Result of Student Class")

s.display("HInal", 26)


class result:
    def __init__(self, name, marksList):
        self.name = name
        self.marksList = marksList
    
    def resultDisplay(self):
        result = sum(self.marksList)
        print("Student Name:", self.name, "Total AVG Marks:", result / len(self.marksList))

r = result("Jay", [90, 80, 70, 60, 50])
r.resultDisplay()

# Static Method in Python

class StaticMethod:
        @staticmethod
        def display():
            print("This is Static Method")

StaticMethod.display()

# Important in Abstraction, Encapsulation, Inheritance, Polymorphism

# Abstraction in Python

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.acc = True
        self.acc = True
        print("Car is started")

car1 = Car()
car1.start()

# Encapsulation in Python

# Wrapping data and functions into a single unit(object)


# Practice

class Account:
    def __init__(self, balance, acccountNo):
        self.balance = balance
        self.accountNo = acccountNo

    def dipoist(self, amount):
        self.balance += amount
        print("Amount Deposited:", amount)
        print("Total Balance:", self.display())

    def withdraw(self, amount):
        self.balance -= amount
        print("Amount Withdrawn:", amount)
        print("Total Balance:", self.display())

    def display(self):
        return self.balance

acc = Account(1000, 101)
acc.dipoist(500)
acc.withdraw(200)