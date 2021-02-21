"""
1. Write a program in Python to find out the character in a string which is uppercase using list
comprehension.
"""
def upper(some_list):
    return ([x for x in some_list if x.isupper()])

