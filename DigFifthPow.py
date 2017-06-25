'''
Digit fifth powers
Problem 30

Surprisingly there are only three numbers that can be written as the sum of fourth
powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth
powers of their digits.

Answer:
443839
'''
import math

def sum_of_pows(n, pow):
    pow_sum = sum([int(x)**pow for x in str(n)])


    return pow_sum

print(sum_of_pows(123,5))

n = 10
total_sum = 0
while(True):
    if n == sum_of_pows(n, 5):
        total_sum += n
        print(total_sum)

    n+=1
