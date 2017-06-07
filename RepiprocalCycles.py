'''
Reciprocal cycles
Problem 26

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest
recurring cycle in its decimal fraction part.

Answer: 983
'''

def repcyclen(i):
    num = 10
    count = 0
    remanders = set()
    while (True):
        #print(num , " mod " , i , num % i )
        rmd = num % i


        if (rmd == 0):
            count = 0
            break

        if not(rmd in remanders):
            count += 1

        if (rmd in remanders):
            count += 1
            break

        if (count == i - 1):
            break

        remanders.add(rmd)
        num = rmd * 10

    return count


maxcyc = 0
maxnumber = 0
cyc = 0



for i in range(15, 1001):
    #print(i)
    cyc = repcyclen(i)

    if(cyc > maxcyc):
        maxcyc = cyc
        maxnumber = i



print(maxnumber)
