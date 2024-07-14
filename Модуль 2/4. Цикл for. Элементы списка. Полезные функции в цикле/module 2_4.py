numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes =[]
not_primes=[]
for i in numbers:
    for j in range(2, (i // 2) + 1):
        if i % j == 0:
            break
        elif i==1 or i==0:
            break
    else:
        primes.append(i)
        not_primes = [x for x in numbers if x not in primes]
print('Primes:',primes)
print('Not Primes:',not_primes)