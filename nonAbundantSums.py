'''
Non-abundant sums
Problem 23

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less
than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper limit
cannot be reduced any further by analysis even though it is known that the
greatest number that cannot be expressed as the sum of two abundant numbers
is less than this limit.Find the sum of all the positive integers which
cannot be written as the sum of two abundant numbers.
'''

def factors(x):

   factors = []
   for i in range(1, x):
       if x % i == 0:
           factors.append(i)

   return factors

def listOfAbundant(x):
    abundants = []

    for i in range(1,x):
        if isAbundant(i):
            abundants.append(i)
    return abundants

def isAbundant(x):

    return sum(factors(x)) > x




abundants = listOfAbundant(28124)

abset = set()

for i in range(0, len(abundants)):
    for j in range(i, len(abundants)):
        absum = abundants[j] + abundants[i]
        if (absum < 28124):
            abset.update({absum})

result = 0
for i in range(1, 28124):
    if i not in abset:
        result += i



print(result)
