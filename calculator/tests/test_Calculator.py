import unittest
from calculator.Calculator import Calculator


class CalculatorTest(unittest.TestCase):
    calculator = Calculator()
    def test_add(self):
        self.assertEqual(4, self.calculator.add(2,2))
        self.assertEqual(3.2, self.calculator.add(1,2.2))

    def test_minus(self):
        self.assertEqual(2, self.calculator.minus(3,1))
        self.assertEqual(-2, self.calculator.minus(1,3))

    def test_multiple(self):
        self.assertEqual(12, self.calculator.multiple(3,4))
        self.assertEqual(13.5, self.calculator.multiple(3,4.5))

    def test_devide(self):
        self.assertEqual(3, self.calculator.devide(9,3))

        # How to deal with Exception in TDD?
        with self.assertRaises(ZeroDivisionError):
            self.calculator.devide(3,0)


if __name__ == "__main__":
    unittest.main()
