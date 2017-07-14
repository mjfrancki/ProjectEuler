"""
Project Euler Problem 37
========================

The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain
prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left
to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
import numpy
from itertools import permutations

def dig_to_list(numbers):
    return int(''.join([ "%d"%x for x in numbers]))

def is_truncatable(num):
    lst = [int(x) for x in str(num)  ]

    for i in range( 1, len(lst) ):
        #print(lst[0:i])
        #numbers = lst[0:i]
        #print ( dig_to_list( lst[0:i] )  )
        #print ( dig_to_list( lst[i: len(lst) ] )  )
        #print( int(''.join(str(i) for i in lst[0:i])) )

        if not ( isPrime(  dig_to_list( lst[0:i] )   ) )  or  not isPrime( dig_to_list( lst[i: len(lst) ] ) ):

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
print("Primes Generate")

sum = 0
for p in primes:
    if is_truncatable(p):
        sum += p
        


print(sum-17)
