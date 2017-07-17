"""
Project Euler Problem 92
========================

A number chain is created by continuously adding the square of the digits
in a number to form a new number until it has been seen before.

For example,

44 32 13 10 1 1
85 89 145 42 20 4 16 37 58 89

Therefore any chain that arrives at 1 or 89 will become stuck in an
endless loop. What is most amazing is that EVERY starting number will
eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""


def chain(num):

    chain = []
    chain.append(num)

    #lst = map(int, str(num) )
    c_sum = 0
    while True:
        lst = map(int, str(num) )

        c_sum = 0
        for i in lst:
            c_sum += i**2

        chain.append(c_sum)

        if c_sum == 1:
            return chain
        if c_sum == 89:
            return chain

        num = c_sum


count = 0
lst = []
for i in range(1,10000000):
    print(i)
    lst = chain(i)
    if lst[len(lst)-1] == 89:
        count += 1

print( count )
