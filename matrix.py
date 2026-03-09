from fraction import Fraction
from mixedFraction import MixedFraction
import numpy as np

class Matrix:
    def __init__(self, row:int, col:int):
        # Instantiate 
        # I thought about implementing this one to create a unit matrix, but decided not to as it wouldn't work for non-square matrices
        self.__matrix = [[0]*row]*col
        self.__row = row
        self.__col = col            
        # self.__isVector = False
        # self.__isSquare = False
    def __init__(self, vector:list[int|str|float|Fraction|MixedFraction]):
        # I am choosing to view vectors as having one column and many rows.
        matrix = []
        for r in vector:
            matrix.append([r])
        self.__matrix = matrix
        self.__row = len(vector)
        self.__col = 1

    def __init__(self, matrix:list[list[int|str|float|Fraction|MixedFraction]]):
        self.__matrix = [[Fraction(x) for x in row] for row in matrix]
        self.__row = len(matrix)
        self.__col = len(matrix[0])

    def get_col(self):
        return self.__col

    def get_row(self):
        return self.__row
    
    def dot(self, other):
        pass

    def cross(self, other):
        # FIXME: should throw error if m1 != n2 or m2 != n1
        for n in range(self.get_col()):
            row1 = self[n]
            for m in range(self.get_row()):
                new_row = []
                pass




    def is_square(self):
        return self.__row == self.__col
    
    def is_vector(self):
        pass

    # def resize(self, row, col):
    #     I might choose not to allow resizing
    #     pass
    # def reset(self, matrix:list[list[int]]):
    #     pass

    def __add__(self, other):
        m1, n1 = self.get_dimension()
        m2, n2 = other.get_dimension()

        if (m1 != m2) or (n1 != n2):
            pass #FIXME should throw error

        output = Matrix(m1, n1)

        for i in range(m1):
            r1 = self[i]
            r2 = other[i]
            new_row = np.add(r1, r2)
            output[i] = new_row
        
        return output



    def mult(self, other):
        pass

    def get_matrix(self):
        return self.__matrix
    
    def __getitem__(self, key):
        # Returns a row of the matrix
        # FIXME: possibly change how get works with double indexing [][]
        return self.__matrix[key]
    
    def __setitem__(self, key, value:list[int|str|float|Fraction|MixedFraction]):
        if len(value) != self.__col:
            pass # FIXME: raise error

        self.__matrix[key] = value
        return value

    def setcell(self, row, col, new_val):
        self.__matrix[row][col] = new_val
        return new_val
    def get_dimension(self):
        return (self.__row, self.__col)
