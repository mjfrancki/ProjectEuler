"""
Project Euler Problem 38
========================

Take the number 192 and multiply it by each of 1, 2, and 3:

  192 * 1 = 192
  192 * 2 = 384
  192 * 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We
will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
and 5, giving the pandigital, 918273645, which is the concatenated product
of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as
the concatenated product of an integer with (1,2, ... , n) where n > 1?

solution: 932718654
Time elapsed: user: 785 ms, sys: 10.5 ms, total: 795 ms
"""

def is_9_pandigt(n):
    lst = [int(i) for i in str(n)]
    list.sort(lst)

    return lst == [1,2,3,4,5,6,7,8,9]

def cat_prod(n, list):

    result = ""
    for num in list:
        prod = n * num
        result += str(prod)

    return result

#n = 2
#while True:
ans = 0
for n in range(2,10000):

    #print(n)

    for max in range(1,n):
        lst = range(1,max)

        catprod = cat_prod( n, lst )

        #print(catprod)

        if len(catprod) > 9:
            break

        if is_9_pandigt(  catprod  ):
            if catprod > ans:
                ans = catprod


    #n += 1

print( ans )
