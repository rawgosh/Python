for num in range(1,20):
    for i in range(2,num):
        if num % i == 0:
            j = num / i
            print("%d equals %d * %d"%(num,i,j))
            break

    else:
        print(num," is a prime numebr")

a = list(range(2,10))
print(a)

