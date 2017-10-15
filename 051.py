"""
Project Euler Problem 51
========================

By replacing the 1st digit of *57, it turns out that six of the possible
values: 157, 257, 457, 557, 757, and 857, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this
5-digit number is the first example having seven primes, yielding the
family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently
56003, being the first member of this family, is the smallest prime with
this property.

Find the smallest prime which, by replacing part of the number (not
necessarily adjacent digits) with the same digit, is part of an eight
prime value family.
"""

import numpy
from itertools import combinations

def replace(num, indexs, replacment):
    digits = str(num)

    for i in indexs:
        digits = digits[:i] + str(replacment) + digits[i + 1:]

    return int(digits)



def combos_with_exclusion(lst, length):
    for combo in combinations((e for e in lst ), length):
        yield list(combo)


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


def getSmallestPrimeFamily(p):

    digits = str(p)

    maxSize = 0
    family = []
    temp = []


    indexs = list(xrange( len(digits) ) )

    #print indexs


    for i in range(1, len(indexs)-1 ):

        for sublist in combos_with_exclusion(indexs, i):
            temp  = []

            for n in range(0,10):

                newNum = replace(p, sublist, n)
                if isPrime( newNum ) and len(str(newNum)) == len(str(p)):
                    temp.append(newNum)

            if len(temp) > maxSize:
                family = temp[:]
                maxSize = len(temp)
            #print sublist
    return family


'''
    for i in range(0, len(digits)):
        for j in range(0, len(digits)):

            if i == j:
                continue

            temp  = []

            for k in range(0,10):


                #if k == 0 and j == 0:
                #    continue

                #if k == 0 and i == 0:
                #    continue


                digits = str(p)
                digits = digits[:i] + str(k) + digits[i + 1:]
                digits = digits[:j] + str(k) + digits[j + 1:]

                newNum = int(digits)
                #print newNum

                print(k, i, j, newNum)


                if isPrime(newNum):

                    temp.append(newNum)
                    #print temp


            if len(temp) > maxSize:
                family = temp[:]
                maxSize = len(temp)
                #print maxSize
'''






print( getSmallestPrimeFamily(121313) )



#print replace(1111111,[1,3,5], 9)



primes = primesfrom2to(1000000)
print "generated primes!"



for prime in primes:
    print prime

    fam = getSmallestPrimeFamily(prime)
    if len(fam) == 8:
        print fam
        print min(fam)
        break
