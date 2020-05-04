'''
Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''
def isHappyNumber(n: int)-> bool:
    while(n!= 1):
        listNums =[]
        while(n>0):
            temp = n%10
            print(temp)
            listNums.append(temp)
            n//=10
        print(listNums)
        sum =0 
        for i in listNums:
            sum  += i**2
        print(sum)
        if sum ==1:
            return True
        n=sum
    return False

print(isHappyNumber(19))