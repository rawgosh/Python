num = int(input('Enter a number: '))
print('Your number is ',num)
for i in range(2,num):
    if num % i == 0:
        j = num / i
        print('Comosite')
        print("%d equals %d * %d"%(num,i,j))
else:
    print(num,' is Prime Number.')

