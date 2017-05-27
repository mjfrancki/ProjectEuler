#Permuted muliples
#problem 52
#It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
#Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
# Answer:142857
def sameDig(a,b):

        if sorted(str(a)) == sorted(str(b)): return True
        return False



start = 1
result = 0
mults =[2]

found = False


while  not found:
   #print(n)
   start  *= 10

   for i in range(start+2,start*10/6,3):
            found = True
            for j in range(2,7,1):
                if not sameDig(i, j*i):
                    found = False
                    break

            if found :
                result = i
                break



print(result)







#print(n)
