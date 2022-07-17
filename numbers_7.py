#NUMBERS

a = 10
print(type(a))
a = 10.6
print(type(a))
a = 1+2j
print(type(a))
print()
print()

#FUNCTINS IN NUMBERS

#ABSOLUTE
num = int(input("Enter a number: "))
print("The absolute value is ",abs(num))
print()
print()

#CEIL
import math
num = float(input("Enter a float number: "))
print(math.ceil(num))
print()
print()


#FLOOR
num = float(input("Enter a number: "))
print(math.floor(num))
print()
print()

#EXPONENTIAL
num = int(input("Enter a number: "))
print(math.exp(num))
print()
print()

#MAX & MIN
a = (12,3,4)
b = (12,3,4)
print(max(a))
print(min(b))
print()
print()

#POW
num = int(input("Enter a number: "))
power = int(input("Enter a power: "))
print(pow(num,power))
print()
print()


#SQRT
print(math.sqrt(100))
print()
print()


#MODF -> it gives seperate integer and float
print(math.modf(12.34))
print()
print()


#LOG
print(math.log(10,10))