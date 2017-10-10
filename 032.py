"""
Project Euler Problem 32
========================

We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once; for example, the 5-digit number, 15234,
is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to
only include it once in your sum.
"""
from sets import Set

def panprod(mult1, mult2):

    x = (str(mult1) + str(mult2))


    if len(x) > len(set(x)): return False

    prod = mult1 * mult2

    x = x + str(prod)

    #print str( mult1 ) + " X " +  str(mult2) + " = " + str( prod )
    digSet = Set(['1','2','3','4','5','6','7','8','9'])

    #print set(x)
    #print digSet

    if len(x) > len(set(x)): return False

    #print type(set(digSet))
    #print type(set(x))


    return set(x) == set(digSet)





print panprod(39,186)



prodSum = 0
prodSet = Set([])


for i in range(1, 9999):
    for j in range(1,9999):
        if i * j > 98901:
            break

        if panprod(i,j):
            prodSet.add(i*j)

            print str( i ) + " X " +  str(j) + " = " + str( i*j )



print sum(prodSet)
