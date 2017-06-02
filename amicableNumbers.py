'''
Amicable Numbers
Problem 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

Answer: 31626
'''


def factors(x):
   # This function takes a number and prints the factors

   factors = []
   for i in range(1, x):
       if x % i == 0:
           factors.append(i)
           #print(i)

   return factors

def d(x):
    return sum(factors(x))

def isAmicable(a):
    b  = d(a)
    db = d(b)

    if( db == a  and a != b ):
        return True

    return False





x = 0

for i in range(2,10000):

    if isAmicable(i):
        x += i



print (x)
