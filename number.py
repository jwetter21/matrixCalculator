"""
This is the Number class, which allows support for math with mixed fractions.
"""


class Number:
    def __init__(self, num:str="0"):
        # Expect inputs of the form "1 1/2", "5/4", "2 7/3", "", "3", "2.345", etc.
        # FIXME: Need input validation
        temp = num.copy()
        # call __convert
        if " " in temp:
            # It is a mixed number
            pass
        if "/" in temp:
            # It contains a fraction
            pass
        # self.__fractionNum = 
        # self.__fractionDen = 
    def __convert(num:str) -> tuple[int]:
        pass
    def __add__(self, other):
        pass
    # also implement for __mul__(), __sub__(), __lt__(), __gt__() and __eq__()
