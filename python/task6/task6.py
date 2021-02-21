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



if __name__ == "__main__":
    students = ['Smit', 'Jaya', 'Rayyan']
    subjects = ['CSE', 'Networking', 'Operating System']
    makeDict(students,subjects)
