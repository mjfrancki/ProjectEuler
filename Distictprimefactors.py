'''
Distinct primes factors
Problem 47

Find the first four consecutive integers to have four distinct prime
factors each. What is the first of these numbers?

'''


def distictFactors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)

    result = len(set(factors))
    return result


#how many consecutive number
consecnum = 4

ans = [consecnum] * consecnum

print(ans)

result = []

number = 646

while True:
    number += 1

    for i in range(0,consecnum):
        result.append( distictFactors(number + i) )


    if result == [4,4,4,4]:
        print number
        break

    result = []
