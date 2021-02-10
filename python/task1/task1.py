"""
1. Create three variables in a single line and assign values to them in such a manner that each one of
them belongs to a different data type.
"""
a, b, c = 1, 'Hello', True

"""
2. Create a variable of type complex and swap it with another variable of type integer.
"""

a = 10
b = 3 + 3j

# swap

c = a
a = b
b = c

"""
3. Swap two numbers using a third variable and do the same task without
using any third variable.
"""

a = 10
b = 20

# swap using a third variable

c = a
a = b
b = c

#swap without using a third variable

a, b = b, a

"""
4. Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x
Version.
"""

#Python 3.x code
str = input('Please enter your input here: \n')
print (str)

#Python 2.x code
#str = raw_input('Please enter your input here: \n')
#print str

"""
5. Write a program to complete the task given below:
Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
another variable called z. Add 30 to z and store the output in variable result and print result as the
final output.
"""

print ('Please enter two numbers between 1-10\n')
number1 = float(input('Please enter the first number: '))
number2 = float(input('Please enter the second number: '))
z = number1 + number2
result = z + 30
print (result)

"""
6. Write a program to check the data type of the entered values.
HINT: Printed output should say - The data type of the input value is : int/float/string/etc
"""

some_input = eval(input('Enter your value here: \n'))
some_type = type(some_input).__name__
print (f'The data type of the input value is {some_type}.')

"""
7. Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and
UPPERCASE.
"""
newVariable = 'lower Camel Case'
NewVariable = 'Upper Camel Case'
new_variable = 'snake _ case'
NEWVARIABLE = 'UPPER CASE'

"""
8. If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’
again. Will it change the value? If Yes then Why?
"""

# It will change because Python is a dynamic language.


#if __name__ == '__main__':


    



