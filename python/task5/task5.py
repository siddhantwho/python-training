from sys import argv

"""
1. Write a program in Python to allow the error of syntax to be handled using exception handling.
HINT: Use SyntaxError
"""
def syntaxCheck():
    try:
        if True:
            x = eval(input('Type your syntactically incorrect input here: \n'))
    except SyntaxError:
        print ('Check your input!')

"""
2. Write a program in Python to allow the user to open a file by using the argv module. If the
entered name is incorrect throw an exception and ask them to enter the name again. Make sure
to use read only mode.
"""
def argvOpen():
    if (argv[1]) != 'hello.txt':
        raise Exception('There\'s no such file!')
    else:

        with open(argv[1], 'r') as my_file:
            print(my_file.read())

"""
3. Write a program to handle an error if the user entered a number more than four digits it should
return “The length is too short/long !!! Please provide only four digits”
"""
def just4():
    x = input('Please enter a number of four digits')
    if len(x) != 4:
        raise ValueError("The length is too short/long !!! Please provide only four digits.")

"""
4. Create a login page backend to ask users to enter the username and password. Make sure to
ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it
should not be more than 3 times.
"""
def passWord():
    Password = 'csgbjv'
    user = input('Please enter a username: \n')
    password = ''
    counter = 0
    while (password != Password) and (counter < 3):
        counter += 1
        password = input('Please enter your password: \n')
    if password == Password:
        print ('Login succesful!')
    else:
        print ('You have run out of attempts!')

"""
5. Go through the link provided below to understand finally and raise concept:
https://www.programiz.com/python-programming/exception-handling
"""

"""
6. Read doc.txt file using Python File handling concept and return only the even length string from
the file. Consider the content of doc.txt as given below:
"""
def evenReader():
    evenlist = []
    with open('doc.txt','r+') as file:
        text = file.read()
        wordlist = text.split()
    for i in wordlist:
        if len(i)%2 == 0:
            evenlist.append(i)
    return (evenlist)


if __name__ == "__main__":
    pass

    

