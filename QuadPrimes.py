'''
Quadratic primes
Problem 27

Euler discovered the remarkable quadratic formula:

n^2 + n = 41
It turns out that the formula will produce 40 primes for the consecutive integer  n 0 to 39



'''


def isPrime(n):
    return all([(n%j) for j in range(2, int(n**0.5)+1)]) and n>1


num = 0
n = 0
count = 0
maxPrimes = 0



for a in range(-1000, 1001):
    print(a)

    for b in range(-1000,1001):

        while(True):
            num = n**2 + a*n + b
            if num > 2:
                if isPrime(num):
                    count += 1
                else:
                    break
            else:
                break
            n += 1

        if count > maxPrimes:
            maxPrimes = count



print(maxPrimes)
