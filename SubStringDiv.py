'''
Sub-string divisibility
Problem 43

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.

Answer:
16695334890
'''
def getNum(numList):
    s = ''.join(map(str, numList))
    return int(s)

def findFirst(nums):

        #for(int i = nums.length-2; i > 0; i--)
        for i in range(len(nums)-2, 0, -1):
            if nums[i] < nums[i+1]:
                 return i
        return 0

def findCeilofFirst(first, nums):
    smallest = 1000000
    indx = -1
    i = 0
    while(first+i < len(nums)-1):
        i += 1
        if nums[first+i] > nums[first] and nums[first+i] < smallest:

            smallest = nums[first+i]
            indx= first+i
    return indx


def divCheck(d):
    if getNum(d[1:4]) % 2 == 0 and getNum(d[2:5])  % 3 == 0 and getNum(d[3:6])  % 5 == 0 and getNum(d[4:7])  % 7 == 0 and getNum(d[5:8])  % 11 == 0 and getNum(d[6:9])  % 13== 0 and getNum(d[7:10])  % 17== 0 :
        return True

    return False


#maxRange = math.factorial(k) / math.factorial((n-k)
    #for x in range(0, maxRange):

PermSum = 0
nums = [0,1,2,3,4,5,6,7,8,9]
#for i in range(0,362880):
while(True):
    first = findFirst(nums)
    second = findCeilofFirst(first, nums)
    #swap(nums, first, second)
    nums[first], nums[second] = nums[second], nums[first]
    #Arrays.sort(nums,first+1,nums.length)
    nums[first+1:len(nums)] = sorted( nums[first+1:len(nums)] )
    #print(nums)


    if divCheck(nums):
        print(nums)
        PermSum += getNum(nums)

    if nums == [9,8,7,6,5,4,3,2,1,0]:
        break

print(PermSum)
