"""
1. Create a list of given structure and get the Access list as provided below:
"""
x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
al1 = x[5][0:4]

al2 = x[6:8]

al3 = x[0::2]

al4 = x[::-1]

al5 = [x[5][5][0]]

al6 = x[0:0]


"""
2. Create a list of thousand numbers using range and xrange and see the difference between each
other.
"""
#list1 = xrange(1,1000)
#list2 = range(1,1000)

"""
3. How Tuple is beneficial as compared to the list?
"""
# Tuple values cannot be changed and therefore can protect variable from
# accidentally being changed.

"""
4. Write a program in Python to iterate through the list of numbers in the range of 1,100 and print
the number which is divisible by 3 and is a multiple of 2.
"""

def divby3or2(arr = range(1,100)):
    for i in arr:
        if i % 3 == 0 and i % 2 == 0:
            print (i)

"""
5. Write a program in Python to reverse a string and print only the vowel alphabet if it exists in the
string with their index.
"""
def reverseVowel(someString):
    reversedString = someString[::-1]
    vowels = ['a','e','i','o','u']
    for i in range(len(reversedString)):
        if reversedString[i] in vowels:
            print (f'{i} {reversedString[i]}')

"""
6. Write a program in Python to iterate through the string “hello my name is abcde” and print the
string which is having an even length.
"""
def evenStrings(hello = 'Hello my name is abcde'):
    stringList = hello.split(' ')
    for i in stringList:
        if len(i) % 2 == 0:
            print (i)

"""
7. Write a program in python to print the pair of numbers whose sum is equal to the result
number that is let's say 8.
"""
def findSum(x = [1,2,3,4,5,6,7,8,9,-1], num = 8):
    complements = list(map(lambda x: 8 - x, x))
    for i in x:
        if i in complements and x.index(i) != complements.index(8 - i):
            print (i, 8 - i)
    print (complements)

            
if __name__ == "__main__":
    findSum()

