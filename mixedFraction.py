"""
Created by Jasmine Hiebert (jwetter21) in February 2026.

This is the MixedFractions class, which allows support for math with mixed fractions.
This performs similar functionality to the Function class, but was created partly 
as a learning experience and partly to be able to deal with mixed numbers in 
addition to fractions.
"""


from fractions import Fraction

class MixedFraction(Fraction):
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

