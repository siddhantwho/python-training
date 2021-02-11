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

"""
if __name__ == "__main__":
    print(capitalise('hello world'))