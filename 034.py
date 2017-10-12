"""
Project Euler Problem 34
========================

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.


answer is 40730 the only answers are 145 and 40585, not sure when to stop
looking
"""

import math


def isDigfact(x):

    num = x
    digits = [int(d) for d in str(x)]
    #print digits

    facted = [math.factorial(x) for x in digits]
    #print facted
    fsum = sum(facted)

    #print num
    #print fsum

    return num == fsum

i = 2
while(True):
    i = i + 1
    if isDigfact(i):
        print i
