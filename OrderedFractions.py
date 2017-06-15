'''
Ordered fractions
Problem 71

Consider the fraction, n/d, where n and d are positive integers. If n<d and
HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d <= 8 in
ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.
By listing the set of reduced proper fractions for d <= 1,000,000 in ascending
order of size, find the numerator of the fraction immediately to the left of 3/7.

'''
from fractions import gcd

def simplify_fraction(numer, denom):

    if denom == 0:
        return "Division by 0 - result undefined"

    # Remove greatest common divisor:
    common_divisor = gcd(numer, denom)
    (reduced_num, reduced_den) = (numer / common_divisor, denom / common_divisor)
    # Note that reduced_den > 0 as documented in the gcd function.

    if reduced_den == 1:
        return "%d/%d is simplified to %d" % (numer, denom, reduced_num)
    elif common_divisor == 1:
        return "%d/%d is already at its most simplified state" % (numer, denom)
    else:
        return "%d/%d is simplified to %d/%d" % (numer, denom, reduced_num, reduced_den)
##Quick method
##3/7
d = 1000000
multFact = 1000000/7

print(multFact)

num = 3*multFact
den = 7*multFact
print(simplify_fraction(num-1, den))

#slow method
d = 8
bar = 3/7.

minDist = 1
dist = 0
resultNum = 0
resultDen = 0

fraction = 0

print(bar)


print(gcd(299999, 700000))

for num in range(1,d+1) :
    for den in range(2,d) :
        #print (num,"/",den ," = ", float(num)/den)
        fraction = float(num)/den
        if fraction  < bar:
            dist = bar - fraction

            if dist < minDist :
                minDist = dist
                resultNum = num
                resultDen = den


            #print (num,"/",den ," = ", float(num)/den)


print(resultNum,"/",resultDen)
#math.gcd(,)
