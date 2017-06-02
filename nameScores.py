'''
Names Scores
Problem 22

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into alphabetical
order. Then working out the alphabetical value for each name, multiply this
value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?


Answer: 871198282
'''

import csv

def alphabeticalValue(s):
    result = 0;
    for c in s:
        result += ord(c)-64
    return result



with open('names.txt', newline='') as inputfile:
    names = list(csv.reader(inputfile))

names = names[0]
names = sorted(names)


total = 0;

for s in range(0, len(names)):
    total += alphabeticalValue(names[s])*(s+1)

print(total)
