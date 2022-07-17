#IF STATEMENT
a = 10
if(a == 10):
    print("Hello World!")

list_variable = ["Hello","World"]
if("Hello" in list_variable):
    print("Siiiiiiiii")

set_variable = {"Ragosh","Shrestha"}
if "Ragosh" in set_variable:
    print("Cool")
print()
print()

#------------------------------------------------------------#

#IF ELIF ELSE STATEMENT
a = int(input("Enter a number: "))
print(a)
if a > 0:
    print("Positive")
elif a < 0:
    print("Negative")
else:
    print("Zero")
print()
print()

#------------------------------------------------------------#

#BREAK STATEMENT

for a in range(4):
    print(a)
    if a == 2:
        break
    print("Hello")
else:
    print("Cool")
print()
print()


for var in "string":
    if var == "i":
        break #IT BREAKS THE LOOP AFTER THE VARIABLE GIVEN IN THE CONDITION IS FOUND
        print(var)
    else:
        print(var)
print("Hello")
print()
print()


#------------------------------------------------------------#

#CONTINUE STATEMENTS
for var in "String":
    if var == "i":
        continue #IT CONTINUES THE LOOP BY REMOVING THE VARIABLE GIVEN IN THE CONDITION
        print(var)
    else:
        print(var)
print()
print()

