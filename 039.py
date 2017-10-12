"""
Project Euler Problem 39
========================

If p is the perimeter of a right angle triangle with integral length
sides, {a,b,c}, there are exactly three solutions for p = 120.

                    {20,48,52}, {24,45,51}, {30,40,50}

For which value of p < 1000, is the number of solutions maximised?
"""

import math
from collections import defaultdict

class Triangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.hyp = math.sqrt( a**2 + b**2 )

    def setA(self, n):
        self.a = n
        hyp = math.sqrt( self.getA()**2 + self.getB()**2 )

    def setB(self, n):
        self.b = n
        hyp = math.sqrt( self.getA()**2 + self.getB()**2 )

    def getA(self):
        return self.a

    def getB(self):
        return self.b

    def getHyp(self):
        return self.hyp

    def printTri(self):
        print self.getA()
        print self.getB()
        print self.getHyp()

    def isIntegral(self):
        return self.getHyp().is_integer()

    def getPerimeter(self):
        return self.getA() + self.getB() + self.getHyp()




tri = Triangle(1,1)

my_dict = defaultdict(int)

for i in range(1,500):
    for j in range(1,500):

        #tri.setA(i)
        #tri.setB(j)
        tri = Triangle(i,j)



        if tri.getPerimeter() > 1000:
            break



        if tri.isIntegral():

            #print tri.getPerimeter()
            my_dict[ tri.getPerimeter() ] += 1
            #print my_dict[ tri.getPerimeter() ]



print max(my_dict, key=my_dict.get)
