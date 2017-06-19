'''
Passcode derivation
Problem 79

A common security method used for online banking is to ask the user for three
random characters from a passcode. For example, if the passcode was 531278,
they may ask for the 2nd, 3rd, and 5th characters;
the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order,
analyse the file so as to determine the shortest possible secret
passcode of unknown length.
Answer:
73162890
'''


#file = open("keylog.txt", "r")

'''
with open(file) as f:
    content = f.readlines()

content = [x.strip() for x in content]

print(content)

'''

import time


def isXY(list,x,y):
    try:
        x_inx = list.index(x)
        y_inx = list.index(y)
    except ValueError:
        return True

    if x_inx > y_inx: return False
    else: return True


with open("keylog.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line)

array = [x.strip() for x in array]


#print(array)

#print(isXY(",1,3))

#initial guess
passcode =[3,1,2,9,7,6,8,0]
code=[]
noChange = True
while(True):
    noChange = True
    for num in array:

        for d in num:
            code.append(int(d))
        #print(code)

        if  not isXY(passcode,code[0],code[1]):


            passcode[passcode.index(code[0])], passcode[passcode.index(code[1])] = passcode[passcode.index(code[1])], passcode[passcode.index(code[0])]
            #print(passcode)
            noChange = False
        if  not isXY(passcode,code[0],code[2]):


            passcode[passcode.index(code[0])], passcode[passcode.index(code[2])] = passcode[passcode.index(code[2])], passcode[passcode.index(code[0])]
            #print(passcode)
            noChange = False
        if  not isXY(passcode,code[1],code[2]):


            passcode[passcode.index(code[1])], passcode[passcode.index(code[2])] = passcode[passcode.index(code[2])], passcode[passcode.index(code[1])]
            #print(passcode)
            noChange = False
        code = []

    if  noChange == True: break


print( ''.join(str(e) for e in passcode))
