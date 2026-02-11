# -*- coding: utf-8 -*-
"""
Jasmine Wetter
CS 161 June 8, 2022
Final Project - Vector Calculator

This program can perform multiple operations involving vectors.
I was inspired to do this project from the material I learned 
in MTH 254 (multivariate claculus) this term (Spring 2022)
"""

import math

class Vector:
    def __init__(self,vector):
        # A string of the form '<2,-4,1>' is inputted and assigned to 
        # self.__vectorString
        self.__vectorString = vector
        
        # vector is used to also create a list containing all of the components
        # of the list; this is helpful for calculations later
        self.__vector = [int(i.strip()) for i in vector[1:-1].split(',')]
        
    def getLength(self):
        # Return the length of the vector (i.e. number of components)
        return len(self.__vector)
    
    def compareLength(self,other):
        # Compares the length of the vector with the length of another vector
        # Returns a Boolean
        if self.getLength() == other.getLength():
            return True
        else:
            return False
    
    def get_vector(self):
        # Return the list of the vector's componets
        return self.__vector
    
    def magnitude(self, squared=False):
        # Calculates the magnitude of the vector
        # Takes a Boolean, squared, as a parameter. Default value is False.
        
        # Square each of the components in the list self.__vector
        componentsSquared = [i*i for i in self.__vector]
        
        # Find the sum of the squared components
        sumComponentsSquared = 0
        for i in componentsSquared:
            sumComponentsSquared += i
        
        # If squared == True, return the magnitude squared as an integer, 
        # else return the magnitude as a float
        if squared:
            return sumComponentsSquared
        else:
            return math.sqrt(sumComponentsSquared)
        
    def __str__(self):
        # When I need to print a vector I want to print the vector string
        return self.__vectorString
    
    def dotProduct(self,other):
        # Calculate the dot product with another vector
        # If the two vectors have a different number of components, print an 
        # error message.
        if len(self.get_vector()) != len(other.get_vector()):
            print("Error. Tried to find the dot product of two vectors "
                  "with a different number of components.")
            return None
        else:
            product = 0
            for i in range(len(self.get_vector())):
                product += self.get_vector()[i] * other.get_vector()[i]
            return product
        
    def add2Vectors(self,other):
        # Find the sum with another vector
        # If the two vectors have a different number of components, print an 
        # error message.
        if len(self.get_vector()) != len(other.get_vector()):
            print("Error. Tried to find the sum of two vectors "
                  "with a different number of components.")
            return None
        else: 
            result = []
            for i in range(len(self.get_vector())):
                result.append(f'{self.get_vector()[i] + other.get_vector()[i]}')
            vectorSum = Vector('<' + ','.join(result) + '>')
            return vectorSum
        
    def multiplyScalar(self,scalar):
        # Multiply the vector with a scalar
        result = [f'{i*scalar}' for i in self.__vector]
        vectorProduct = Vector('<' + ','.join(result) + '>')
        return vectorProduct
    
    def crossProduct(self,other):
        # Find the cross product with another vector
        # Only perform calculations if the two vectors have the same length
        # and have three components each.
        if self.compareLength(other) and self.getLength() == 3:
            componentList1 = self.get_vector()
            componentList2 = other.get_vector()
            component0 = (componentList1[1] * componentList2[2]) - (componentList1[2] * componentList2[1])
            component1 = -((componentList1[0] * componentList2[2]) - (componentList1[2] * componentList2[0]))
            component2 = (componentList1[0] * componentList2[1]) - (componentList1[1] * componentList2[0])
            outVector = Vector('<' + f"{component0},{component1},{component2}" +'>')
            return outVector
        else:
            return None
        


def print_menu():
    # Print the menu
    print("VECTOR MENU\n"
          "a - add two vectors together (returns a vector)\n"
          "s - multiply a vector with a scalar (returns a vector)\n"
          "d - find the dot product of two vectors (returns a scaler)\n"
          "c - find the cross product of two vectors (only for vectors with three components, returns a scalar)\n"
          "m - find the magnitude of a vector (answer is rounded to 4 decimal places, returns a scalar)\n"
          "n - find the squared magnitude of a vector (answer is exact, returns a scalar)\n"
          "u - find a unit vector with the same direction as a given vector (answer is rounded to 4 decimal places, returns a vector)\n"
          "i - Get more information and/or an example of one of the above items\n"
          "q - quit\n")

def createVector():
    '''
    This function takes a string input from the user and ensures that it is 
        of the proper form to create a Vector object. Then it creates a Vector 
        object from the user's input.

    Returns
    -------
    vector : Vector

    '''
    # Ensure that the user's vector is of the proper form for the program to work
    properVector = False
    while not properVector:
        possibleVector = input("Enter a vector (ex. <2,-4,1>):\n").strip()
        properVector = True
        for i in possibleVector:
            # Check for any characters that are not allowed
            if (not (i.isdigit() or i == ',' or i.isspace() or i == '<' or i == '>' or i == '-')):
                properVector = False
            # Check to make sure the '<' and '>' aren't in the wrong place
            elif possibleVector.index(i) != 0 and i == '<':
                properVector = False
            elif possibleVector.index(i) != (len(possibleVector)-1) and i == '>':
                properVector = False
            # If the vector is not valid, inform the user
            if not properVector:
                print("The vector you entered is not valid. A valid vector "
                      "contains only numbers, negative signs, commas, '<' and "
                      "'>'. The '<' and '>' are optional.")
                break
    
    
    # If the user did not include the '<' or '>' or added to much whitespace
    # then fix it so that it works for the calculations.
    possibleVector = ','.join([i.strip() for i in possibleVector.split(',')])
    if possibleVector[0] == '<' and possibleVector[-1] == '>':
        vector = possibleVector
    elif possibleVector[0] == '<':
        vector = possibleVector + '>'
    elif possibleVector[-1] == '>':
        vector = '<' + possibleVector
    else:
        vector = '<' + possibleVector + '>'
    
    # When the vector is ready, turn it into a Vector object
    vector = Vector(vector)
    
    # Return the Vector object
    return vector

def get2VectorsEqualLength():
    # Some calculations require that two vectors have the same number of 
    # components. This function makes sure that they do.
    v1 = createVector()
    v2 = createVector()
    while not v1.compareLength(v2):
        print("\nI'm sorry, the two vectors you entered are not the same "
              "length. In order to perform this calculation, the two vectors "
              "must have the same number of components. Please try again.")
        v1 = createVector()
        v2 = createVector()
    return v1, v2

def printInfo():
    # Give the user more information / examples of the possible calculations
    
    infoDict = {"a":"Option 'a' finds the sum of two vectors by finding "
                    "the sum of each of their components. For example, if "
                    "you have two vectors <3,0,-9> and <-1,5,10>, then "
                    "their sum is <3+-1,0+5,-9+10> or <2,5,1>.",
                "s":"Option 's' multiplies each of a vector's components "
                    "with a scalar value (in this case meaning an "
                    "integer). For example The vector <7,-9,-1> multiplied "
                    "with the scalar -2 is the vector <-2*7,-2*-9,-2*-1> "
                    "or <-14,18,2>.",
                "d":"Option 'd' finds the dot product of two vectors. "
                    "Dot product only works for two vectors with the same "
                    "number of components. "
                    "Dot product is calculated by finding the product of "
                    "each of the components in each vector and then "
                    "finding the sum of the resulting sums. The dot "
                    "product of two vectors returns a scalar. "
                    "For example, given two vectors <9,2,-5> and <3,6,7>, "
                    "the dot product is (9*3)+(2*6)+(-5*7) = 27+12+-35 = 4.",
                "c":"Option 'c' finds the cross product of two vectors. "
                    "Cross product only works for two vectors with three "
                    "components each. The cross product of two vectors "
                    "yields a third vector which is orthogonal to both of "
                    "the original vectors. For example, given two vectors "
                    "<2,0,-1> and <1,-3,-2>, the cross product is "
                    "<((0*2)-(-1*-3)),-((2*-2)-(-1*1)),((2*-3)-(0*1))> "
                    "= <(0-3),-(-4--1),(-6-0)> = <-3,3,-6>. "
                    "Note that, when finding the cross product, the order "
                    "of the vectors does matter, so the cross product of "
                    "<2,0,-1> and <1,-3,-2> (in that order) is <-3,3,6>, "
                    "but the cross product of <1,-3,-2> and <2,0,-1> is "
                    "<3,-3,6>.",
                "m":"Option 'm' finds the magnitude of a vector. "
                    "Magnitude is calculated as the square root of the sum "
                    "of each of the components squared in a vector. For "
                    "example, the magnitude of the vector <2,4,1> is "
                    "sqrt((2^2)+(4^2)+(1^2)) = sqrt(4+16+1) = sqrt(21) "
                    "which is approximately 4.5826. "
                    "Because square roots often result in irrational "
                    "answers, this program rounds magnitude to four "
                    "decimal places.",
                "n":"Option 'n' returns the squared magnitude of a vector. "
                    "Because calculating the magnitude involves finding a "
                    "square root (see information on 'm') which often "
                    "results in an irrational number this program rounds "
                    "magnitudes to 4 decimal places. In case the user "
                    "wants a more exact answer, the user can use option "
                    "'n' to get the magnitude squared which (in the case "
                    "of this program) will be an integer and, hence, will "
                    "be an exact answer. For "
                    "example, the magnitude squared of the vector <2,4,1> is "
                    "(2^2)+(4^2)+(1^2) = 4+16+1 = 21.",
                "u":"Option 'u' returns a unit vector with the same direction "
                    "as a given vector. A unit vector is a vector with a "
                    "magnitude of 1. A unit vector with the same direction "
                    "as a given vector can be calculated by dividing each "
                    "component of the given vector by the magnitude of "
                    "the given vector. For example, the magnitude of the "
                    "vector <3,-1,-3> is approximately 4.3589 and, thus, "
                    "a unit vector with (approximately) the same direction "
                    "as <3,-1,-3> is <3/4.3589,-1/4.3589,-3/4.3589> = "
                    "<0.6882,-0.2294,-0.6882>. Note that (for the purposes "
                    "of this program) the components in the unit vector will "
                    "usually be approximate and rounded to 4 decimal places "
                    "since the magnitude is usually approximate."}
    
    # Print options for the user to get information on
    print("\nGET INFORMATION ON ONE OF THESE OPTIONS\n"
          "a - add two vectors together (returns a vector)\n"
          "s - multiply a vector with a scalar (returns a vector)\n"
          "d - find the dot product of two vectors (returns a scaler)\n"
          "c - find the cross product of two vectors (only for vectors with three components, returns a scalar)\n"
          "m - find the magnitude of a vector (answer is rounded to 4 decimal places, returns a scalar)\n"
          "n - find the squared magnitude of a vector (answer is exact, returns a scalar)\n"
          "u - find a unit vector with the same direction as a given vector (answer is rounded to 4 decimal places, returns a vector)\n"
          "e - returns all information\n")
    
    # Get coice from user
    infoChoice = input("Which option in the menu would you like more "
                       "information on?\n")
    
    # Make sure choice is a valid option
    while infoChoice != 'a' and infoChoice != 's' and infoChoice != 'd' and infoChoice != 'm' and infoChoice != 'n' and infoChoice != 'c' and infoChoice != 'u' and infoChoice != 'e':
        print("\nPlease enter one of the options in the above list.\n")
        infoChoice = input("Which option in the menu would you like more "
                           "information on?\n")
    print()
    
    # Either print all of the information or just some of it based on user input
    if infoChoice == 'e':
        # Print all information
        choices = sorted(infoDict.keys())
        for l in choices:
            print(f"{l}: {infoDict[l]}\n")
    else:
        # Print information on just one item from the options
        print(infoDict[infoChoice])

def execute_menu(option):
    # This function executes based on the menu option that the user selects.
    
    if option =='m':
        # Create the vector from user input
        vector = createVector()
        
        # Calculate and return the magnitude
        print(f"\nThe magnitude of {vector} is approximately {vector.magnitude():.4f}.")
        
    elif option == 'u':
        # Find a unit vector with the same direction as a given vector
        
        # Get vector from user
        vector = createVector()
        
        # Calculate unit vector
        unitVector = '<' + ','.join([f'{i/vector.magnitude():.4f}' for i in vector.get_vector()]) + '>'
        
        # Return unit vector
        print(f"\nA unit vector with the same direction as {vector} is approximately {unitVector}.")
        
    elif option == 'd':
        # Get two vectors of the same length
        vector1,vector2 = get2VectorsEqualLength()
        
        # Find the dot product of the two vectors and return to user
        newVector = vector1.dotProduct(vector2)
        print(f"\nThe dot product of {vector1} and {vector2} is {newVector}.")
        
    elif option == 'a':
        # Get two vectors of the same length
        vector1,vector2 = get2VectorsEqualLength()
        
        # Add the two vectors together and return output (another vector) to user
        newVector = vector1.add2Vectors(vector2)
        print(f"\nThe sum of {vector1} and {vector2} is {newVector}.")
    
    elif option == 's':
        # Get a vector 
        vector = createVector()
        
        # Get a scalar
        scalar = int(input("What scalar value would you like to multiply with "
                           "your vector?\n"))
        
        # Calculate the new vector and return to user
        newVector = vector.multiplyScalar(scalar)
        print(f"\nThe scalar {scalar} times the vector {vector} is {newVector}.")
    
    elif option == 'c':
        # Get two vectors of the same length
        vector1,vector2 = get2VectorsEqualLength()
        
        # Make sure the length of the vectors is 3
        while vector1.getLength() != 3:
            print("\nI'm sorry, you can only find the cross product of two "
                  "vectors with three components each. Please try again.")
            vector1,vector2 = get2VectorsEqualLength()
        
        # Calculate and return cross product
        newVector = vector1.crossProduct(vector2)
        print(f"\nThe cross product of {vector1} and {vector2} is {newVector}.")
    
    elif option == 'n':
        # Create the vector from user input
        vector = createVector()
        
        # Calculate and return the magnitude squared
        print(f"\nThe magnitude squared of {vector} is {vector.magnitude(True)}.")
    
    elif option == 'i':
        printInfo()

def main():
    print("Hello. My name is MathBot. This is the vector calculator. Please "
          "select what you would like to do from the vector menu.")
    choice = ''
    
    # This program will run until the user enters 'q'
    while choice != 'q':
        print()
        print_menu()
        choice = input("Please enter your choice:\n")
        
        # Make sure that the user's choice is a valid option
        while choice != 'i' and choice != 'a' and choice != 's' and choice != 'd' and choice != 'c' and choice != 'm' and choice != 'n' and choice != 'u' and choice != 'q':
            choice = input("Please enter an option from the above menu:\n")
        
        if choice != 'q':
            execute_menu(choice)
    
    # When done say goodbye.
    print("\nGoodbye.")

if __name__ == '__main__':
    main()