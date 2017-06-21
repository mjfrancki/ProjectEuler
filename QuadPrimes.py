'''
Quadratic primes
Problem 27

Euler discovered the remarkable quadratic formula:

n2+n+41n2+n+41
It turns out that the formula will produce 40 primes for the
consecutive integer values 0 <= n <= 390 <= n <= 39. However,
when n=40,402+40+41=40(40+1)+41 is divisible by 41,
and certainly when n=41,412+41+41 is clearly divisible by 41.

The incredible formula n^2 - 79n+1601 was discovered, which produces
80 primes for the consecutive values 0<=n<=79. The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

n2+an+b , where |a|<1000 and |b| <= 1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |-4| =4
Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n, starting with n=0.

'''
import numpy

def primesfrom2to(n):

    sieve = numpy.ones(n/3 + (n%6==2), dtype=numpy.bool)
    for i in xrange(1,int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k/3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)/3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]


def isPrime(n):
    i = 0

    while (primes[i] <= n):
        if (primes[i] == n):
            return True
        i += 1

    return False


maxCount = 0
maxA = 0
maxB = 0

primes = primesfrom2to(100000000)
bPrimes = primesfrom2to(1000)

print("Generated Primes")

for a in range(-999,-1,2):
    for b in bPrimes:
        print(a,b)
        n = 0

        while(abs(isPrime(n**2 + a*n + b))):
            n += 1

        if n > maxCount:

            maxCount = n
            maxA = a
            maxB = b



print(maxA*maxB)
print(maxA,maxB)
print(count)
