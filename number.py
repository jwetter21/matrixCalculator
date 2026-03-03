"""
Created by Jasmine Hiebert (jwetter21) in February 2026.

This is the Number class, which allows support for math with mixed fractions.
This performs similar functionality to the Function class, but was created partly 
as a learning experience and partly to be able to deal with mixed numbers in 
addition to fractions.
"""


from fractions import Fraction

class Number(Fraction):
    # The code for this function was created partially with help and debuggin from ChatGPT on 3-2-2026.
    def __new__(cls, value):
        # If it's already numeric, let Fraction handle it
        if isinstance(value, (int, float, Fraction)):
            return super().__new__(cls, value)

        # If it's a string, parse it
        if isinstance(value, str):
            value = value.strip()

            # Mixed number case: "a b/c"
            if " " in value:
                whole_str, frac_str = value.split()

                whole = int(whole_str)

                numer_str, denom_str = frac_str.split("/")
                numer = int(numer_str)
                denom = int(denom_str)

                # Handle negative whole numbers correctly
                if whole < 0:
                    numer = -abs(numer)

                improper = whole * denom + numer
                return super().__new__(cls, improper, denom)

            # Regular fraction like "3/4"
            if "/" in value:
                numer_str, denom_str = value.split("/")
                return super().__new__(cls, int(numer_str), int(denom_str))

            # Just an integer string like "5"
            return super().__new__(cls, int(value))

        raise TypeError("Unsupported type for Number")

# from fractions import Fraction

# class Number(Fraction):
#     def __init__(self, input:str):
#         temp = input

#         if " " in temp:
#             # It is a mixed number
#             components = temp.split(" ")
#             if len(components) == 2 and (components[0].isdigit() or components[0][1:].isdigit()):
#                 whole += int(components[0]) 
#                 temp = components[2]
            
#                 if "/" in temp:
#                     # It contains a fraction
#                     num_denom = temp.split("/")
#                     numer = int(num_denom[0])
#                     denom = int(num_denom[1])
#                     # # FIXME: check for bad input, this assumes good input
#                     # if numer >= denom:
#                     #     whole += numer // denom
#                     #     # temp = 

#                     improperFractionNumerator = (whole * denom) + numer
#                     improperFractionDenomenator = denom
#                     super().__init__(improperFractionNumerator, improperFractionDenomenator)
#                 else:
#                     Fraction(input)
#             else:
#                 Fraction(input)
#         else:
#             Fraction(input)

    
    # def __new__(cls, whole=0, numerator=0, denominator=1):
    #     if denominator == 0:
    #         raise ZeroDivisionError("Denominator cannot be zero")

    #     if whole < 0:
    #         numerator = -abs(numerator)

    #     improper_numerator = whole * denominator + numerator
    #     return super().__new__(cls, improper_numerator, denominator)

    # def __str__(self):
    #     whole = self.numerator // self.denominator
    #     remainder = abs(self.numerator % self.denominator)

    #     if remainder == 0:
    #         return str(whole)
    #     elif whole == 0:
    #         return f"{self.numerator}/{self.denominator}"
    #     else:
    #         return f"{whole} {remainder}/{self.denominator}"

# class Number:
#     def __init__(self, num:str="0", precision=5):
#         # Expect inputs of the form "1 1/2", "5/4", "2 7/3", "", "3", "2.345", etc.
#         # FIXME: Need input validation
#         self.__improperFractionNumerator = 0
#         self.__improperFractionDenomenator = 1
#         temp = num.copy().strip() # strip any leading or ending whitespace

#         # consider using regular expressions rather than if statements for cleaner code
#         # [0-9]+
#         # [1-9][0-9]* [0-9]+/[1-9][0-9]*
#         # [0-9]+/[1-9][0-9]*
#         # /0 => div by zero error

#         whole = 0
#         # call __convert
#         if " " in temp:
#             # It is a mixed number
#             components = temp.split(" ")
#             if len(components) != 2:
#                 pass
#                 # raise error?
#             elif not components[0].isdigit():
#                 pass
#                 # raise error
#             else:
#                 whole += int(components[0])
#                 temp = components[2]
#         if "/" in temp:
#             # It contains a fraction
#             num_denom = temp.split("/")
#             numer = int(num_denom[0])
#             denom = int(num_denom[1])
#             # FIXME: check for bad input, this assumes good input
#             if numer >= denom:
#                 whole += numer // denom
#                 # temp = 

#         self.__improperFractionNumerator = whole + (numer % denom)
#         self.__improperFractionDenomenator = denom

#         # self.__wholeComponent = 
#         # self.__fractionNumerator = 
#         # self.__fractionDenomenator = 

#     def __convert(num:str) -> tuple[int]:
#         pass
#     def __add__(self, other):
#         pass
#     def __subtract__(self, other):
#         pass

#     # also implement for __mul__(), __sub__(), __lt__(), __gt__() and __eq__()
