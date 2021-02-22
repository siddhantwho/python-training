"""
1. Write a program in Python to find out the character in a string which is uppercase using list
comprehension.
"""
def upper(some_string):
    return ([x for x in some_string if x.isupper()])

"""
2. Write a program to construct a dictionary from the two lists containing the names of students and
their corresponding subjects. The dictionary should map the students with their respective subjects.
Let’s see how to do this using for loops and dictionary comprehension.
"""
def makeDict(somekeys,somevals):
    items = list(zip(somekeys,somevals))
    
    return {k:v for (k,v) in items}

"""
3. Learn More about Yield, next and Generators
"""

"""
4. Write a program in Python using generators to reverse the string.
Input String = “Consultadd Training”
"""
def reverser(some_string):
    n = len(some_string)
    for i in range(n-1,-1,-1):
        yield some_string[i]

# to print the letters of the reversed string in a sequence
for i in reverser('batman'):
    print (i)

# to generate a new string in the reversed order
newstr = ''
for i in reverser('batman'):
    newstr = newstr + i

"""
5. Write an example on decorators.
"""
def decorator(some_function):
    def wrapper():
        print('This is what my function does: \n')
        #does whatever the function some_function would do
        some_function()
    return wrapper

@decorator
def greeter():
    print ('Hello world')

if __name__ == "__main__":
    greeter()
