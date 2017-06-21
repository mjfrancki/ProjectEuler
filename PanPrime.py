'''
Pandigital prime
Problem 41


We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
and is also prime.

What is the largest n-digit pandigital prime that exists?

'''

import numpy
from itertools import permutations


def listGen(n):
    lst = range(1,n+1)
    lst  = [str(i) for i in lst]
    return lst


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

def isPandig(num):
    lst = [int(i) for i in str(num)]
    lst.sort()
    length = len(lst)
    return lst == range(1,length+1)




primes = primesfrom2to(987654321)
print("Primes Generated")

perms = [''.join(p) for p in permutations(['1','2','3','4','5','6','7','8','9'])]
perms  = map(int, perms)



results = []

for n in range(9,1,-1):

    perms = [''.join(p) for p in permutations(listGen( n ))]
    perms  = map(int, perms)

    result = set(perms).intersection(primes)
    if len(result) > 0:
        print(max(result))
        break
