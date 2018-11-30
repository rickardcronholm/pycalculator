"""
Implemets and runs test of calculator.Calculator
"""

import unittest
from calculator.Calculator import Calculator


class CalculatorTest(unittest.TestCase):
    """unittest.TestCase class"""
    calculator = Calculator()
    def test_add(self):
        """Tests add"""
        self.assertEqual(4, self.calculator.add(2, 2))
        self.assertEqual(3.2, self.calculator.add(1, 2.2))

    def test_minus(self):
        """Tests minus"""
        self.assertEqual(2, self.calculator.minus(3, 1))
        self.assertEqual(-2, self.calculator.minus(1, 3))

    def test_multiple(self):
        """Tests multiple"""
        self.assertEqual(12, self.calculator.multiple(3, 4))
        self.assertEqual(13.5, self.calculator.multiple(3, 4.5))

    def test_devide(self):
        """Tests devide"""
        self.assertEqual(3, self.calculator.devide(9, 3))

        # How to deal with Exception in TDD?
        with self.assertRaises(ZeroDivisionError):
            self.calculator.devide(3, 0)


if __name__ == "__main__":
    unittest.main()
