#ARITHEMETIC OPERATORS


a=10
b=20
print(a)
print(b)

#ADDITION
c=a+b
print(c)

#MULTIPLICAION
d=a*c
print(d)

#DIVISION
e=d/b
f=d//b
print(e)
print(f)

#MODULUS
f=e%2
print(f)

#TYPE OF DATA
print(type(e))

#EXPONENT
g=a**3
print(g)
print()
print()

#------------------------------------------------------------#

#COMPARISION OPERATORS


a=9
b=8

#GREATER THAN
print(a>b)

#LESS THAN
print(a<b)

#GREATER THAN EQUAL
print(a>=b)

#LESS THAN EQUAL
print(a<=b)

#EQUAL TO
print(a==b)

#NOT EQUAL TO
print(a!=b)
print()
print()

#------------------------------------------------------------#

#ASSIGNMENT OPERATORS


#ASSIGN VALUE
a=10
b=20


#ADDS RIGHT SIDE VALUE TO LEFT SIDE VALUE AND ASSIGN THER RESULT TO LEFT VARIABLE
a += b
print(a)


#SUBTRACTS RIGHT SIDE VALUE FROM LEFT SIDE VALUE AND ASSIGN THEIR RESULT TO LEFT VARIABLE
a -= b
print(a)


#MULTIPLIES RIGHT SIDE VALUE WITH LEFT SIDE VALUE AND ASSIGN THEIR RESULT TO LEFT VARIABLE
a *= b
print(a)


#DIVIDES LEFT SIDE VALUE WITH RIGHT SIDE VALUE AND ASSIGN THEIR RESULT TO LEFT VARIABLE
a /= b
print(a)


#CALCULATES THE MODULUS USING TWO SIDE VALUES AND ASSIGN THE RESULT TO LEFT VARIABLE
a %= b
print(a)


#CALCULATES THE EXPONENTIALS USING TWO SIDE VALUES AND ASSIGN THE RESULT TO LEFT VARIABLE
b **= 2
print(b)
print()
print()

#------------------------------------------------------------#

#BITWISE OPERATORS


a = 19
b = 18
c = "{0:b}".format(a) #CHECKS THE BINARY FORMAT OF THE INTEGER
d = "{0:b}".format(b)
print(c)
print(d)


#BINARY AND
#10011
#10010
#-----
#10010
#IT COMPARES ACCORDING TO THE TRUTH TABLE IF BOTH ARE '1' THEN THE RESULTANT IS '1' ELSE '0'
print(a & b)


#BINARY OR
#10011
#10010
#-----
#10011
print(a | b)


#BINARY XOR
#10011
#10010
#-----
#00001
print(a ^ b)


#BINARY COMPLEMENT
print(~a)
print(~-18)


#LEFT SHIFT
a = 100
c = "{0:b}".format(a)
print(a)
print(c)
print(a << 2)


#RIGHT SHIFT
print(a>>2)
print()
print()

#------------------------------------------------------------#

#LOGICAL OPERATORS


a = 15
b = 20

#AND
#RETURNS TRUE IF BOTH STATEMENTS ARE TRUE
print(a<20 and b<30)


#OR
#RETURNS TRUE IF ONE OF THE STATEMENTS IS TRUE
print(a%3==0 or b%3==0)


#NOT
#REVERSE THE RESULT, RETURNS FALSE IF THE RESULT IS TRUE
print(not(a<20 and b<30))
print()
print()

#------------------------------------------------------------#

#MEMBERSHIP AND IDENTITY OPERATORS


#IN
a = "Ragosh"
b = "18"
list_data_type = ["Ragosh","Itachi","99","4"]
print(a in list_data_type) #CHECKS WHETHER THE VALUE OF "a" IS IN "list_data_type" OR NOT


#NOT IN
print(b not in list_data_type)


#IS
a = 10
b = 9
print(a is b) #COMPARES THE MEMOORY LOCATION OF TWO VARIABLES


#IS NOT
print(a is not b)
print()
print()