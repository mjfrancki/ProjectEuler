'''
Maximum path sum II
Problem 67
By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and
'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.
Answer:
7273
'''
def rowCombine(top, bottom):
    x = [0]*len(top)
    for i in range(0, len(top)):

        x[i] = ( top[i] + max(bottom[i],bottom[i+1]) )

    return x


file = open("triangle.txt", "r")


triangle = [0]*100
print(triangle)

for n in range(0,100):
    line = file.readline()
    line = line.split()
    line = [int(i) for i in line]


    triangle[n] = line

    #triangle[n] = file.readline()



#print(triangle)


for i in reversed(range(0,99)):
    triangle[i] = ( rowCombine( triangle[i], triangle[i+1] ) )

print( triangle[0] )
