#LISTS

a = ['ragosh',1474,'rawgosh22787']
print(a)

#LIST MODIFICATION

#ACCESS
print(a[1])

#UPDATE
a[1] = 'hiiii'
print(a)

#DELETE
del a[2]
print(a)

#MAX AND MIN
print(max(a))
print(min(a))

#COUNT -> IT COUNTS THE REPEATED NUMBERS INSIDE THE LIST
b = [1,2,3,4,5,4,3,4,5,6,7,3,4,2,4,5,6]
print(b.count(7))

#INDEX -> IT FINDS THE INDEX OF THE ITEM
c = [10,20,30,40]
print(c.index(30))

#APPEND
c.append(50)
print(c)

#INSERT -> IT IS SAME LIKE APPEND BUT WE CAN PROVIDE INDEX
c.insert(2,25)
print(c)

#REVERSE
c.reverse()
print(c)

#SORT -> ARRANGES IN ASCENDING ORDER
b.sort()
print(b)
b.reverse()
print(b)