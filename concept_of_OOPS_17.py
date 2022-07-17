#OOP -> Object Oriented Programming

#Object -> An object is an instance of a class. It exists in real world.
#Class -> Blueprint for the Object.




class Employee:
    def __init__(self,name,post,salary):
        #init method is used to initialize a data inside the class so that the variable can be used anywhere inside the class
        #self is a parameter that represents the class. We use self whenever we have different object.
        self.name = name
        self.post = post
        self.salary = salary
        

    def work(self):
        print("My name is "+self.name+".")
        print("I am "+self.post+".")
        print("I earn $",self.salary)

"""
s1 = Employee('Ragosh','Engineer',999999999)
print(s1.name)
s1.work()
"""

n = str(input("Enter your name :"))
a = str(input("Enter your post :"))
b = int(input("Enter your Salary :"))
s2 = Employee(n,a,b)
s2.work()

#Inheritance -> It is the ability of a class to inherit the properties of another class.

#Single level -> Single inheritance enables a derived class to inherit properties from a single parent class.
#Multi level -> Multilevel inheritance is one type of inheritance being used to inherit both base class and derived class features to the newly derived class.


class Learn:
    def __init__(self,name,book):
        self.name = name
        self.book = book


class School:
    def sch(self):
        print("I want to read.")


class Library(Learn,School):
    def study(self):
        print(self.name+" is reading "+self.book)


name = str(input("Enter your name :"))
book = str(input("Enter the book you are reading :"))
s = Library(name,book)
s.study()
s.sch()
