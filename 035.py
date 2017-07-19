"""
Project Euler Problem 35
========================

The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
71, 73, 79, and 97.

How many circular primes are there below one million?
"""


import numpy

def to_num(number):
    return int(''.join(str(i) for i in number))

def rotate(l, x):
    return l[-x:] + l[:-x]

def is_circlur_prime(n):
    lst = [int(d) for d in str(n)]

    for i in range(1, len(lst) ):
        if not isPrime( to_num( rotate(lst,i) ) ):
            return False

    return True


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

count = 0
for p in primes:
    if is_circlur_prime(p):
        count += 1


print(count)
