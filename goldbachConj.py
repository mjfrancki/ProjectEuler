'''
Goldbach's other conjecture
Problem 46

It was proposed by Christian Goldbach that every odd composite number
can be written as the sum of a prime and twice a square.

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime
and twice a square?

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


def primePlusTwiceSquare(number, primes):
    limit = int(round(numpy.sqrt(number/2)))+1
    #print(limit)
    for i in range(1, number):
        for j in range(1, limit):
             #print("%d + %d = %d  "%(primes[i],2*(j**2), primes[i] + 2*(j**2) ))
             if primes[i] + 2*(j**2) == number:
                #print("%d + %d = %d  "%(primes[i],2*(j**2), primes[i] + 2*(j**2) ))
                return True
    return False


primes = primesfrom2to(100000)
number = 1


#print(primePlusTwiceSquare(25, primes))


while True:
    number += 2

    if not isPrime(number):
        if not primePlusTwiceSquare(number,primes):
            print(number)
            break
