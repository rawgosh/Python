#STRINGS

a = "ragosh"

#CAPITALIZE -> IT RETURNS THE SAME STRING WITH FIRST LETTER CAPITAL
print(a.capitalize())

#COUNT -> IT COUNTS THE NUMBER OF CHARACTER IN THE STRING
print(a.count('a'))

#FIND -> IT FINDS THE INDEX POSITION OF CHARACTER
print(a.find('g'))

#ALPHANUMERIC
print("ragosh129".isalnum())

#ALPHA
print('123'.isalpha())

#DIGIT
print('123'.isdigit())

#LENGTH
print(len(a))

#LOWER
print(a.lower())

#UPPER
print(a.upper())

#SWAPCASE
#CAPITAL -> INTO SMALL AND SMALL INTO CAPITAL
print(a.swapcase())

#MAX & MIN
print(max(a))
print(min(a))

#REPLACE -> IT REPLACES THE CHARACTER
print(a.replace('r','s'))