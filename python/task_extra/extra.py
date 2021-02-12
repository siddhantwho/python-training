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
def findPairs(x = [1,2,3,4,5,6,7,8,9,-1], num = 8):
    used = []
    for i in range(len(x)):
        if ((num - x[i]) in x[i+1:]):
            print (x[i], num - x[i])

"""
8. Write a program in Python to complete the following task:
> Create two lists such as even_list and odd_list
> Ask user to enter a number in the range of 1,50 and make sure if the entered number is
even, append it to the even_list and if the entered number is odd append it to the odd_list.
> Keep that in mind you can only add 5 items in each list
> Make sure once you enter all the 5 elements, calculate the sum of the list and return the
maximum of the list.
"""

def listMaker():
    evenList = []
    oddList = []
    
    while len(evenList) < 5 and len(oddList) < 5: 
        newNum = int(input('Please enter a number in the range 1 - 50\n'))
        if newNum % 2 == 0:
            evenList.append(newNum)
        else:
            oddList.append(newNum)
    finalList = evenList if len(evenList) > len(oddList) else oddList

    return (f'The sum of the list is {sum(finalList)} and the max is {max(finalList)}')

"""
9. Write a program to find out the occurrence of a specific character from an alphanumeric string.
Sample input: 12abcbacbaba344ab
Expected output: a=5 b=5 c=2
NOTE: Make sure to avoid counting the occurrence of numeric values in the string.
"""

def countChar(somestr):
    alphaList = []
    for i in somestr:
        if i.isalpha():
            alphaList.append(i)
    alphaSet = set(alphaList)
    for i in alphaSet:
        print (f'{i} = {alphaList.count(i)}')

"""
10. Generate and print another tuple whose values are even numbers in the given tuple
(1,2,3,4,5,6,7,8,9,10).
"""

    
def returnEven(someTup = (1,2,3,4,5,6,7,8,9,10)):
    evenList = []
    for i in someTup:
        if i % 2 == 0:
            evenList.append(i)
    return (tuple(evenList))

            
if __name__ == "__main__":
    pass

