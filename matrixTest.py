import unittest
from matrix import Matrix
from fraction import Fraction
from mixedFraction import MixedFraction

class TestMatrix(unittest.TestCase):
    def test_init(self):
        A = Matrix([[3,-13/12, 6.5],[33/4, '1 1/7', -1.2],['-88/90', 0.99, 5]])

        self.assertEqual(A[0][1], MixedFraction(-13/12))
        self.assertEqual(A[2][0], MixedFraction('-88/90'))

if __name__ == '__main__':
    unittest.main()