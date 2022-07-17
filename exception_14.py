# Errors detected during execution are called exceptions.

from pickle import TRUE


while TRUE:
    try: #The try block lets you test a block of code for errors
        a = int(input("Enter an integer value :"))
        break
    except: #The except block lets you handle the error.
        print("Please! Use only integers :(")
    finally: #The finally block lets you execute code, regardless of the result of the try- and except blocks.
        print("Thank You :)")