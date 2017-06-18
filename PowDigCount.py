'''
Powerful digit counts
Problem 63

The 5-digit number, 16807=7^5, is also a fifth power. Similarly,
the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?

answer 49 
'''


def nthPowers(n):
    count = 0
    base = 1
    number = 0
    while(True):
        number = base ** n
        #print(number)

        if len(str(number)) == n:
            count += 1

        if len(str(number)) > n:
            break
        base += 1
    return count


count = 0

n = 1
while(True):
    count += nthPowers(n)

    if nthPowers(n) == 0:
        break

    n += 1
    #print(count)

print(count)
