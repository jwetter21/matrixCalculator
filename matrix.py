
class Matrix:
    def __init__(self, row:int, col:int):
        # Instantiate 
        self.__matrix = [[0]*row]*col
        self.__row = row
        self.__col = col            
        # self.__isVector = False
        # self.__isSquare = False
    def __init__(self, vector:list[int]):
        # I am choosing to view vectors as having one column and many rows.
        self.__matrix = [vector]
        self.__row = len(vector)
        self.__col = 1

    def __init__(self, matrix:list[list[int]]):
        self.__matrix = matrix
        self.__row = len(matrix)
        self.__col = len(matrix[0])

    def col(self):
        pass
    def row(self):
        pass
    def dot(self, other):
        pass
    def cross(self, other):
        pass
    # def resize(self, row, col):
    #     I might choose not to allow resizing
    #     pass
    def reset(self, matrix:list[list[int]]):
        pass
    def add(self, other):
        pass
    def mult(self, other):
        pass
    def get_matrix(self):
        return self.__matrix
