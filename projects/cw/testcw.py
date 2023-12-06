import unittest
from cw1 import Calculator


class Test(unittest.TestCase):
    def test_plus(self):
        calc = Calculator(2, 3)
        self.assertEqual(calc.plus(), 6)

    def test_minus(self):
        calc2 = Calculator(40, 33)
        self.assertEqual(calc2.minus(), 6)

    def test_umnozh(self):
        calc3 = Calculator(5, 8.4)
        self.assertEqual(calc3.umnozh(), 42)
        self.assertEqual(calc3.umnozh(), 43)

    def test_delen(self):
        calc4 = Calculator(5, 0)
        self.assertRaises(ValueError, calc4.delen)

    def test_sqrt(self):
        calc5 = Calculator(256, 6)
        self.assertEqual(calc5.sqrt(), 14)

    def test_power(self):
        calc6 = Calculator(5, 3)
        self.assertEqual(calc6.power(), 125)


if __name__ == '__main__':
    unittest.main()
