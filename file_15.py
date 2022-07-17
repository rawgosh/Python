#FILE -> It is the name location used to store information/data permanently store in the computer for future access.

#WRITE
file = open("learn.txt",'w') #'w' mode creates a file.
string = str(input("Enter Your name :"))
a = len("My name is "+string+".") #It counts the no of character from the instruction and variable
file.write("My name is "+string+".\n")
file.write("Hello World!\n") #It is used to write inside the document same like print function used to display in the terminal.
file.write("Programming is fun.\n")
file.write("Self learning is super efficient.\n")
file.close() #It closes the file which is opened in any type of mode.
print()

#READ
file = open("learn.txt","r")#'r' mode reads from existing file
print(file.read(a)) #It is used to read the desired information from the existing file.
print(file.tell()) #It tells the current position inside the file.
print("This is the current position of file cursor :)")
file.seek(5) #Returns file cursor to the initial position
print(file.tell())
file.close()
print()

file = open("learn.txt","r")
for line in file: #Using for loop to read the lines inside the file.
    print(line) #It returns line by line.
file.close()
print()

file = open("learn.txt","r")
print(file.readlines()) #It returns all the lines in list format.
file.close()
print()

#APPEND
file = open("learn.txt","a") #'a' mode is used to write in an exixting file.
age = int(input("Enter your age :"))
file.write("I am %d years old."%(age))
file.close()

file = open("learn.txt","r")
print(file.readlines())
file.close()


