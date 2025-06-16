class Matrix:
    def __init__(self, row:int, col:int):
        self.__matrix = [[0]*row]*col
            
        # self.__isVector = False
        # self.__isSquare = False
    def __init__(self, vector:list[int]):
        pass
    def __init__(self, matrix:list[list[int]]):
        pass
    def col(self):
        pass
    def row(self):
        pass
    def dot(self, other):
        pass
    def cross(self, other):
        pass
    def resize(self, row, col):
        pass
    def add(self, other):
        pass
    def mult(self, other):
        pass
    def get_matrix(self):
        return self.__matrix
