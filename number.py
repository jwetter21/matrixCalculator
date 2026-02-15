"""
This is the Number class, which allows support for math with mixed fractions.
"""


class Number:
    def __init__(self, num:str="0", precision=5):
        # Expect inputs of the form "1 1/2", "5/4", "2 7/3", "", "3", "2.345", etc.
        # FIXME: Need input validation
        self.__improperFractionNumerator = 0
        self.__improperFractionDenomenator = 1
        temp = num.copy()

        whole = 0
        # call __convert
        if " " in temp:
            # It is a mixed number
            components = temp.split(" ")
            if len(components) != 2:
                pass
                # raise error?
            elif not components[0].isdigit():
                pass
                # raise error
            else:
                whole += int(components[0])
                temp = components[2]
        if "/" in temp:
            # It contains a fraction
            num_denom = temp.split("/")
            numer = int(num_denom[0])
            denom = int(num_denom[1])
            # FIXME: check for bad input, this assumes good input
            if numer >= denom:
                whole += numer // denom
                # temp = 

        self.__improperFractionNumerator = whole + (numer % denom)
        self.__improperFractionDenomenator = denom
        
        # self.__wholeComponent = 
        # self.__fractionNumerator = 
        # self.__fractionDenomenator = 

    def __convert(num:str) -> tuple[int]:
        pass
    def __add__(self, other):
        pass
    def __subtract__(self, other):
        pass
    # also implement for __mul__(), __sub__(), __lt__(), __gt__() and __eq__()
