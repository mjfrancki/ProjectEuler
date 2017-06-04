'''
Consecutive Prime Sum
Problem 50

Using python 2

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime
below one-hundred. The longest sum of consecutive primes below one-thousand
that adds to a prime, contains 21 terms, and is equal to 953.
Which prime, below one-million, can be written as the sum of the
most consecutive primes?



'''


import numpy



def isPrime(n):
    return all([(n%j) for j in range(2, int(n**0.5)+1)]) and n>1

def primesfrom2to(n):

    sieve = numpy.ones(n/3 + (n%6==2), dtype=numpy.bool)
    for i in xrange(1,int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k/3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)/3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]


primes = primesfrom2to(1000000)

sum = 0
maxCount = 0
ans = 0


for i in range(0, len(primes) - 21 ):
    for j in range(0, 1000000 - i ):
        sum += primes[i+j]
        if sum > 1000000 : break

        if isPrime(sum):
            if j > maxCount:
                maxCount = j
                ans = sum


    sum = 0

print(ans)
