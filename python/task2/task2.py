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
    choice = eval(input(message))
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
2. Write a program in Python to perform the following operator based task:
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

def positiveLoop():
    while (1 == 1):
        x = eval(input('Enter a number: '))
        if (x >= 0):
            print ('Good Going')
            continue
        else:
            print ('It\'s over')
            break

def findMultiples(num1 = 7, num2 = 5):
    range_min = 2000
    range_max = 3200

    for i in range()


if __name__ == "__main__":

    positiveLoop()

    

