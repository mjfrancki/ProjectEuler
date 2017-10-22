'''
Project Euler Problem 206
=========================

Find the unique positive integer whose square has the form
1_2_3_4_5_6_7_8_9_0, where each _ is a single digit.
'''

import re

p = re.compile('1[0-9]2[0-9]3[0-9]4[0-9]5[0-9]6[0-9]7[0-9]8[0-9]9[0-9]0')

n = 1389019170
m = p.match( str(n*n) )
if m:
    print m.group()
else:
    print "no"
#m = p.match("1020304050608080900")


n = 1389026620

while(True):
    m = p.match( str(n*n) )

    if m:
        print('Match found: ', m.group())
        print(n)
        break
    else:
        print("no match")
        n -= 2



'''
i = 1000000000
while(True):
    i += 1

    num = 1**1
    m = p.match( str(num) )

    if not (m is None):
        break


print(num)
'''
