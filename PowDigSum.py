'''
Powerful digit sum
Problem 56

A googol (10100) is a massive number: one followed by one-hundred zeros;
100100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100,
what is the maximum digital sum?

Answer: 972
'''

def digSum(n):
    r = 0
    while n:
       r, n = r + n % 10, n // 10
    return r

maxSum = 0

for a in range(1,100):
    for b in range(1,100):
        number = (a**b)
        if digSum(number) > maxSum:
            maxSum = digSum(number)

print(maxSum)
