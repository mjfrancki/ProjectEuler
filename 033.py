"""
Project Euler Problem 33
========================

The fraction 49/98 is a curious fraction, as an inexperienced
mathematician in attempting to simplify it may incorrectly believe that
49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less
than one in value, and containing two digits in the numerator and
denominator.

If the product of these four fractions is given in its lowest common
terms, find the value of the denominator.
"""
from fractions import gcd
denominator = 10

def commonDigit(a, b):

    dset = set(map(int, str(a))).intersection(map(int, str(b)))

    if  0 in dset:
        dset.remove(0)

    return dset


def digRemove(num, dig):

    return int( str(num).replace(str(dig), "") )



print commonDigit(12344, 44451)


'''
while(True):

    for numerator in range(1, denominator):
        print numerator
        print denominator

    denominator += 1
'''

numProd = 1
demProd = 1
for dem in range(11,99):
    for num in range(10, dem):

        if len( commonDigit(num, dem) ) != 0 :
            #print (num , " / " ,dem)



            for x in commonDigit(num, dem):


                try:
                    newNum = digRemove(num, x)
                    newDem = digRemove(dem, x)

                    if (num /float(dem)) == (newNum / float(newDem)):
                        print (num , " / " ,dem)
                        print (newNum , " / " ,newDem)
                        print ""

                        numProd *= newNum
                        demProd *= newDem



                except ValueError:
                    pass
                    #print "skip"
                except ZeroDivisionError:
                    pass
                    #print "skip"


print "Answer: "
demProd /= gcd(numProd, demProd)
print demProd
