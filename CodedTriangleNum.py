'''
Python 3
The nth term of the sequence of triangle numbers is given by, tn = 1/2n(n+1);
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value.
For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the
word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K
text file containing nearly two-thousand common English words, how many are triangle words?

Answer:
162
'''


import csv

def alphabeticalValue(s):
    result = 0;
    for c in s:
        result += ord(c)-64
    return result

def isTriangle(x):
    if x == 1 : return True
    for n in range(1, x):
        #print(n**2 , "+", n , "/", 2, " = ", (n**2 + n)/2.0 )
        if x == 0.5*n*(n+1) :
            return True
    return False

with open('words.txt', newline='') as inputfile:
    words = list(csv.reader(inputfile))

words = words[0]


count = 0

for n in range(1,100):
    print(n, 0.5*n*(n+1) )

for s in range(0, len(words)):
    if isTriangle( alphabeticalValue(words[s])):
        count += 1

print(count)
