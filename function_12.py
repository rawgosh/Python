def hello_world():
    print("HELLO WORLD!")
hello_world()


#ARGUMENTS -> It is a value that is sent to the function when it is called
def learn(a): #here a is the argument and the function executes only when the argument has a value
    print("Hello :)")
a = 13414
learn(a)

#KEYWORD ARGUMENT
def age(age):
    print(age)
age(18)

#DEFAULT ARGUMENT -> It is a argument that assumes the default value when the value is not provided during a function call

def coordinate(x,y=6):
    print(x,y)
coordinate(4)

#VARIABLE LENGTH ARGUMENT -> It is used when we do not know how many argument will be there in a function
def variable(a,*b):
    print(a)
    for c in b:
        print(c)
variable(1,2,3,4,5,6)

def form(name,age,grade):
    print("Welcome! "+name+".")
    print("It is recorded you are %d years old."%(age))
    print("You are currently in garde %d."%(grade))
name = str(input("Enter your name :"))
age = int(input("Enter your age :"))
grade = int(input("Enter your grade :"))
form(name,age,grade)


def marks(*marks):
    print("Your total mark is :",(marks[3]))
marks(20,30,40,50,60)


#PASS BY VALUE -> Here only the copy of the variable is passed to the function so any change made is affected only to the copied value not the original value.
def program(a):
    a = 16
    if (a > 0):
        print(a," is Natural number")
    else:
        print("Number")
a = 0
program(a)
print(a," is a whole number")

#PASS BY REFERENCE -> Here we pass the actual variable and not the copied variable so any change made to the object inside a function is seen outside of the function aswell.
ref = [123,245,457,878] 
def reference(a):
    a.append(447)
    print(a)
reference(ref)
print(ref)
