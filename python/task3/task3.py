"""
1. Create a list of 10 elements of four different data types like int,
string, complex and float.
"""
newList1 = [1,3.5,7,'eight','apples', 1+2j, 'root -1', 10.2, 9, 10 + 10j]

"""
2. Create a list of size 5 and execute the slicing structure
"""
newList2 = [0,1,2,3,4]
lessThan2 = newList2[0:2]

"""
3. Write a program to get the sum and multiply of all the items in a given list.
"""
def listSum(someList):
    return sum(list)

def listProduct(someList):
    product = 1
    for i in someList:
        product = product * i
    return product

"""
4. Find the largest and smallest number from a given list.
"""
newList4 = [1,99,101]
min4 = min(newList4)
max4 = max(newList4)

"""
5. Create a new list which contains the specified numbers after removing the even numbers from a
predefined list.
"""
allList = [1,2,3,4,5,6,7,8,9,10]

def removeEven(someList):
    for i in someList:
        if (i%2 == 0):
            someList.remove(i)
    return someList

oddList = removeEven(allList)

"""
6. Create a list of elements such that it contains the squares of the first and last 5 elements between
1 and30 (both included).
"""
newList6 = [1**2, 2**2, 3**2, 4**2, 5**2, 26**2, 27**2, 28**2, 29**2, 30**2]

"""
7. Write a program to replace the last element in a list with another list.
"""
def changeLast(someList, listToAdd):
    someList.extend(listToAdd)

"""
8. Create a new dictionary by concatenating the following two dictionaries:
"""

a={1:10,2:20}
b={3:30,4:40}
a.update(b)

"""
9. Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1
and n(both 1 and n included).
"""
def squareDict(n):
    newDict = {}
    for i in range(n):
        newDict[i+1] = (i+1)**2
    return newDict

"""
10. Write a program which accepts a sequence of comma-separated numbers from console and
generates a list and a tuple which contains every number in the form of string.
"""

def ListandTuple():
    numbers = input('Please enter comma separated input here: \n')
    inputList = numbers.split(',')
    inputTuple = tuple(inputList)
    print (inputList, inputTuple)

if __name__ == "__main__":
    pass







