from functools import reduce
"""
1. Write a program to reverse a string.
"""

def reverse(str):
    return (str[::-1])

"""
2. Write a function that accepts a string and prints the number of uppercase letters and lowercase
letters.
"""
def caseCount(str):
    uC = 0
    lC = 0
    for i in str:
        if (i.isupper()):
            uC += 1
        if (i.islower()):
            lC += 1
    print (f'No. of Uppercase characters: {uC} \n No. of Lowercase characters: {lC}')

"""
3. Create a function that takes a list and returns a new list with unique elements
of the first list.
"""
def unique(someList):
    return list(set(someList))

"""
4. Write a program that accepts a hyphen-separated sequence of words as input and
prints the words in a hyphen-separated sequence after sorting them alphabetically.
"""
def wordSort(str):
    wordList = str.split('-')
    wordList.sort()
    newSeq = wordList[0]
    for i in range(1, len(wordList)):
        newSeq = newSeq + '-' + wordList[i]
    print (newSeq)

"""
5. Write a program that accepts a sequence of lines as input and prints the lines after making all
characters in the sentence capitalized.
"""
def capitalise(str):
    capitalStr = ''
    for i in str:
        capitalStr = capitalStr + i.capitalize()
        
    return capitalStr

"""
6. Define a function that can receive two integral numbers in string form and compute their sum and
print it in the console.
"""
def sumFromStr(num1, num2):
    print (int(num1) + int(num2))

"""
7. Define a function that can accept two strings as input and print the string with the maximum length
in the console. If two strings have the same length, then the function should print both the strings line
by line.
"""
def findLong(str1, str2):
    if (len(str1)> len(str2)):
        print (str1)
    elif (len(str2)>len(str1)):
        print (str2)
    else:
        print (str1)
        print (str2)

"""
8. Define a function which can generate and print a tuple where the values are square of numbers
between 1 and 20 (both 1 and 20 included).
"""
def generateSquare():
    squareList = []
    for i in range(1, 21):
        squareList.append(i**2)
    print (tuple(squareList))

"""
9. Write a function called showNumbers that takes a parameter called limit. It should print all the
numbers between 0 and limit with a label to identify the even and odd numbers.
"""

def showNumbers(limit):
    for i in range(limit+1):
        label = 'EVEN' if (i%2 == 0) else 'ODD'
        print (f'{i} {label}')

"""
10. Write a program which uses filter() to make a list whose elements are even numbers between 1
and 20 (both included)
"""
def filterEven(n=20):
    numList = []
    for i in range(1,n+1):
        numList.append(i)
    evenList = list(filter(lambda x: x % 2 == 0, numList))
    return evenList

"""
11. Write a program which uses map() and filter() to make a list whose elements are squares of even
numbers in [1,2,3,4,5,6,7,8,9,10].
Hints: Use filter() to filter even elements of the given listUse map() to generate a list of squares of the
numbers in the filtered list. Use lambda() to define anonymous functions.
"""

def evenSquares(someList = list(range(1,11))):
    evenList = list(filter(lambda x: x % 2 == 0, someList))
    evenSquareList = list(map(lambda y: y**2, evenList))
    return evenSquareList

"""
12. Write a function to compute 5/0 and use try/except to catch the exceptions
"""
def divByZero():
    try:
        result = 5/0
    except:
        print ('Cannot divide by zero')

"""
13. Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().
"""
def reducer(inputList = list(range(1,8))):
    someList = [0]
    someList.extend(inputList)
    flatList = reduce(lambda x,y: x + y*10**(len(someList)-1-someList.index(y)),someList)
    return flatList

"""
14. Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
Make sure to use only higher order functions.
"""
#Given some input values
def sevenNot3(arr):
    result = list(filter(lambda x: x % 7 == 0 and x % 3 != 0, arr))
    return result

#Without input values but upper limit
def sevenNotThree2(limit):
    answers = []
    multiplier = 0
    while (7*multiplier < limit):
        if 7*multiplier % 3 != 0:
            answers.append(7*multiplier)
        multiplier+= 1
    return answers

"""
15. Write a program in Python to multiply the elements of a list by itself using a traditional function
and pass the function to map() to complete the operation.
"""
def multiply(x):
    return (x*x)

def arrayProduct(arr):
    return list((map(multiply, arr)))

"""
16. What is the output of the following codes:
"""
# (i) 2

# (ii)
# after f
# after f?




if __name__ == "__main__":
    x = range(1,20)
    print (list(x))