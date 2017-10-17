"""
Project Euler Problem 60
========================

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two
primes and concatenating them in any order the result will always be
prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The
sum of these four primes, 792, represents the lowest sum for a set of four
primes with this property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.
"""
import numpy
from itertools import combinations


def combos(lst, length):
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


primesto= 20000
primes = primesfrom2to(primesto)


print "generated primes!"


primeLength = len((primes))




indexs = list(xrange( primesto ) )

'''
for sublist in combos(indexs, 5):
     print(sublist)
'''
print( primeLength )

for a in range(0, primeLength):
    #print( primes[a] )


    #print("_______________")
    #print ( str(primes[a] ), str(primes[b]), str(primes[a] ) + str(primes[b])  ,str(primes[b]) + str(primes[a]) )

    for b in range(0, primeLength):
        if( a == b ): continue
        if(  ( not isPrime(int( str(primes[a]) + str(primes[b]) ) ) ) or ( not isPrime(int( str(primes[b]) + str(primes[a]) ) ) )   ): continue

        #print ( str(primes[a] ), str(primes[b]), str(primes[a] ) + str(primes[b])  ,str(primes[b]) + str(primes[a]) )

        for c in range(0, primeLength):
            if (c == b): continue


            if(  not isPrime(int( str(primes[c]) + str(primes[a]) ) ) ): continue
            if(  not isPrime(int( str(primes[c]) + str(primes[b]) ) ) ): continue
            if(  not isPrime(int( str(primes[a]) + str(primes[c]) ) ) ): continue
            if(  not isPrime(int( str(primes[b]) + str(primes[c]) ) ) ): continue


            #print( str(primes[a]) ,str(primes[b]) ,str(primes[c]) )
            #print ( str(primes[a]), str(primes[b]), str(primes[c]), ( str(primes[c] + str(primes[a])) ),  ( str(primes[c])+ str(primes[b])) , (str(primes[a]) + str(primes[c]) ), (str(primes[b]) + str(primes[c]) ) )

            for d in range(0, primeLength):

                if (d == c): continue

                if(  not isPrime(int( str(primes[d]) + str(primes[a]) ) ) ): continue
                if(  not isPrime(int( str(primes[d]) + str(primes[b]) ) ) ): continue
                if(  not isPrime(int( str(primes[d]) + str(primes[c]) ) ) ): continue

                if(  not isPrime(int( str(primes[a]) + str(primes[d]) ) ) ): continue
                if(  not isPrime(int( str(primes[b]) + str(primes[d]) ) ) ): continue
                if(  not isPrime(int( str(primes[c]) + str(primes[d]) ) ) ): continue




                for e in range(0, primeLength):
                    if (e == d): continue

                    if(  not isPrime(int( str(primes[e]) + str(primes[a]) ) ) ): continue
                    if(  not isPrime(int( str(primes[e]) + str(primes[b]) ) ) ): continue
                    if(  not isPrime(int( str(primes[e]) + str(primes[c]) ) ) ): continue
                    if(  not isPrime(int( str(primes[e]) + str(primes[d]) ) ) ): continue

                    if(  not isPrime(int( str(primes[a]) + str(primes[e]) ) ) ): continue
                    if(  not isPrime(int( str(primes[b]) + str(primes[e]) ) ) ): continue
                    if(  not isPrime(int( str(primes[c]) + str(primes[e]) ) ) ): continue
                    if(  not isPrime(int( str(primes[d]) + str(primes[e]) ) ) ): continue


                    print (primes[a], primes[b], primes[c],primes[d],primes[e],  primes[a]+primes[b]+primes[c]+primes[d]+primes[e] )
                    #if(  ( not isPrime(int( str(e) + str(d) ) ) ) or ( not isPrime(int( str(d) + str(e) ) ) )): continue


                    #print (a,b,c,d,e)
