import unittest
from matrix import Matrix
from fraction import Fraction

class TestMatrix(unittest.TestCase):
    def test_init(self):
        A = Matrix([[3,-13/12, 6.5],[33/4, '1 1/7', -1.2],['-88/90', 0.99, 5]])

        self.assertEqual(A.get_matrix[0][1], Fraction(-13/12))
        self.assertEqual(A.get_matrix[2][0], Fraction('88/90'))

if __name__ == '__main__':
    unittest.main()