from number import Number
from fraction import Fraction
import unittest

class TestNumber(unittest.TestCase):
    def setUp(self):
        pass

    def test_add(self):
        x = Number("1 1/2")
        y = Number("13/3") 
        z = x+y
        self.assertEqual(z, Fraction("35/6")) # FIXME: I don't know if I want addition to return a Fraction object
        # self.assertIsInstance(z, Fraction)
        # 13/3 = 4 1/3
        # 1.5 + 4.333 = 5.333
        # self.assertEqual(z, Number("5 5/6"))
        # self.assertEqual(z, "5 5/6")
        # self.assertEqual(z, 5.83333)
    
    def test_subtract(self):
        pass

    # def test_eq_overload_string(self):
    #     x = Number("1 1/3")
    #     self.assertEqual(x, "1 1/3")
    #     # Should I test the other direction too?
    
    def test_instantiate(self):
        x = Number("1")
        y = Number("4/3")
        z = Number("2 3/4")
        self.assertIsInstance(x, Number)
        self.assertIsInstance(y, Number)
        self.assertIsInstance(z, Number)


if __name__ == '__main__':
    unittest.main()