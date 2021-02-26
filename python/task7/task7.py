"""
1. Write a program that calculates and prints the value according to the given formula:
Q= Square root of [(2*C*D)/H]
Following are the fixed values of C and H:
C is 50.
H is 30.
D is a variable whose values should be input to your program in a comma-separated sequence.
"""
class Q:
    def __init__(self):
        self.C = 50
        self.H = 30
    
    def result(self, D):
        for i in D:
            print ((2*self.C*i/self.H))

"""
2. Define a class named Shape and its subclass Square. The Square class has an init function which
takes length as argument. Both classes have an area function which can print the area of the shape
where Shape’s area is 0 by default.
"""
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length**2

"""
3. Create a class to find three elements that sum to zero from a set of n real numbers
Input array: [-25,-10,-7,-3,2,4,8,10]
Expected output: [[-10,2,8],[-7,-3,10]]
"""
class Sum3Zero:
    def __init__(self, somelist):
        self.elements = somelist
    
    def sumLists(self):
        num_set = set(self.elements)
        n = len(self.elements)
        Triplets = []
        for i in range(n):
            for j in range(i+1,n):
                req = (self.elements[i] + self.elements[j])*-1
                triplet = [self.elements[i],self.elements[j],req]
                triplet.sort()
                if (req in num_set) and (triplet not in Triplets):
                    Triplets.append(triplet)
        return Triplets


"""
4. Create a Time class and initialize it with hours and minutes.
Create a method addTime which should take two Time objects and add them.
E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
Create another method displayTime which should print the time.
Also create a method displayMinute which should display the total minutes in the Time.
E.g.- (1 hr 2 min) should display 62 minute.
"""

class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    
    def addTime(self, timeObjToAdd):
        self.hours = self.hours + timeObjToAdd.hours
        self.minutes = self.minutes + timeObjToAdd.minutes

    def displayTime(self):
        print (f'{self.hours} : {self.minutes}')

    def displayMinutes(self):
        totalMins = self.hours*60 + self.minutes
        print (totalMins)
        

"""
5. Write a Person class with an instance variable “age” and a constructor that takes an integer as a
parameter. The constructor must assign the integer value to the age variable after confirming the
argument passed is not negative; if a negative argument is passed then the constructor should set
age to 0 and print “Age is not valid, setting age to 0”. In addition, you must write the following instance
methods:
"""

class Person:
    def __init__(self, age):
        if self.age >= 0:
            self.age = age
        else:
            self.age = 0
            print ("Age is not valid, setting age to 0.")

    def yearPasses(self, years):
        self.age = self.age + years

    def amIOld(self):
        if self.age < 13:
            print ('You are young.')
        elif self.age >= 13 and self.age <=19:
            print ('You are a teenager.')
        else:
            print ('You are old.')



if __name__ == "__main__":
    pass