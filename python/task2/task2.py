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
    



    

if __name__ == "__main__":
    chooseOp()
    

