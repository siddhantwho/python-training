"""
1. Write a program in Python to perform the following operation:
"""
def divBy3Or5(number):

    if ((number % 3 == 0) and (not number % 5 == 0)):
        print ('Consultadd')
    elif ((not number % 3 == 0) and (number % 5 == 0)):
        print ('Python Training')
    elif ((number % 3 == 0) and (number % 5 == 0)):
        print ('Consultadd - Python Training')

"""
2. Write a program in Python to perform the following operator based task:
"""
def chooseOp():
    choices = [1, 2, 3, 4, 5]
    message = """
        Please choose one of the following options:\n
        1 - Addition\n
        2 - Subtraction\n
        3 - Division\n
        4 - Multiplication\n
        5 - Average\n

        Your choice: 
        """
    choice = int(input(message))
    if ((choice!=5) and (choice in choices)):
        print ('You will have to choose 2 numbers!')
        num1 = float(input('Enter the first number: '))
        num2 = float(input('Enter the second number: '))

        if (choice == 1):
            result = num1 + num2
        elif (choice == 2):
            result = num1 - num2
        elif (choice == 3):
            result = num1 / num2
        elif (choice == 4):
            result = num1 * num2

    elif (choice == 5):
        print ('You will have to choose 4 numbers!')
        num1 = float(input('Enter the first number: '))
        num2 = float(input('Enter the second number: '))
        first = float(input('Enter the first number: '))
        second = float(input('Enter the second number: '))
        result = (num1 + num2 + first + second)/4

    else:
        yn = input('Invalid choice! Do you want to try again? y/n \n')
        if (yn == 'y'):
            chooseOp()

    if (result):
        if (result < 0):
            print ('NEGATIVE')
        else:
            print (result)

"""
3. Write a program in Python to implement the given flowchart:
"""

def arithmetic():
    a = 10
    b = 20
    c = 30

    avg = (a + b + c)/3
    print (f'avg = {avg}')

    if ((avg > a) and (avg > b) and (avg > c)):
        print ('avg is higher than a, b, c.')
    else:
        if ((avg > a) and (avg > b)):
            print ('avg is higher than a, b.')
        elif ((avg > a) and (avg > c)):
            print ('avg is higher than a, c.')
        elif ((avg > b) and (avg > c)):
            print ('avg is higher than b, c')
        elif (avg > a):
            print ('avg is just higher than a.')
        elif (avg <= a):
            if (avg > b):
                print ('avg is just higher than b.')
            elif (avg > c):
                print ('avg is just higher than c.')

"""
4. Write a program in Python to break and continue if the following cases occurs:
"""

def positiveLoop():
    while (1 == 1):
        x = float(input('Enter a number: '))
        if (x >= 0):
            print ('Good Going')
            continue
        else:
            print ('It\'s over')
            break

"""
5. Write a program in Python which will find all such numbers which are divisible by 7 but are not a
multiple of 5, between 2000 and 3200.
"""

def findMultiples():
    requiredNumbers = []
    for i in range(286,457):
        number = 7*i
        if (number % 5 != 0):
            requiredNumbers.append(number)
    
    print (requiredNumbers)

"""
6. What is the output of the following code examples?
"""
# TypeError: 'int' object is not iterable

# 0
# error
# 1
# error
# 2

#0
#1
#2
#3
#4

"""
7. Write a program that prints all the numbers from 0 to 6 except 3 and 6.
Expected output: 0 1 2 4 5
Note: Use ‘continue’ statement
"""

def zeroToSix():
    for i in range(7):
        if ((i == 3) or (i == 6)):
            continue
        else:
            print (i)

"""
8. Write a program that accepts a string as an input from the user and calculate the number of digits
and letters.
"""
def counter():
    some_input = input('Enter your string here: \n')
    letters = 0
    digits = 0
    for i in some_input:
        if (i.isnumeric()):
            digits += 1
        else:
            letters += 1
    print (f'Letters: {letters} \nDigits: {digits}')

"""
9. Read the two parts of the question below:
> Write a program such that it asks users to “guess the lucky number”. If the correct number is
guessed the program stops, otherwise it continues forever.
> Modify the program so that it asks users whether they want to guess again each time. Use two
variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want
to continue guessing. The program stops if the user guesses the correct number or answers “no”.
The program continues as long as a user has not answered “no” and has not guessed the correct
number
"""

def luckyNumber(luck):
    number = int(input('Guess the lucky number: '))
    if (number == luck):
        print ('Congratulations')
    else:
        answer = input('Wrong answer! Do you want to continue guessing? yes/no \n')
        if (answer == 'no'):
            print ('Goodbye!')
        else:
            luckyNumber(luck)

"""
10. Write a program that asks five times to guess the lucky number. Use a while loop and a counter,
such as

While counter <= 5:
print(“Type in the”, counter, “number”
counter=counter+1
The program asks for five guesses (no matter whether the correct number was guessed or not). If the
correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”.
After the fifth guess it stops and prints “Game over!”.
"""

def fiveTries(luck):
    counter = 1
    while (counter <= 5):
        guess = int(input(f'Type in guess number {counter}: \n'))
        if (guess == luck):
            print ('Good guess!')
        elif (counter < 5):
            print ('Try again!')
        
        counter += 1
    print ('Game over!')

"""
11. In the previous question, insert break after the “Good guess!” print statement. break will terminate
the while loop so that users do not have to continue guessing after they found the number. If the user
does not guess the number at all, print “Sorry but that was not very successful”.
"""

def fiveTries2(luck):
    correct = False
    counter = 1
    while (counter <= 5):
        guess = int(input(f'Type in guess number {counter}: \n'))
        if (guess == luck):
            print ('Good guess!')
            correct = True
            break
        elif (counter < 5):
            print ('Try again!')
        
        counter += 1
    if not (correct):
        print ('Sorry but that was not very succesful.')



        



if __name__ == "__main__":

    fiveTries2(21)

    

