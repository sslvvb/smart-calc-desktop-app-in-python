"""
Unit tests for the calculator module.
"""

import unittest

import calculator


class TestCalculator(unittest.TestCase):
    """Test cases for the Calculator class."""

    def test_calculate_1(self):
        result = calculator.calculate("sin(1+15)*14^1-36/2.4")
        self.assertAlmostEqual(float(result), -19.0306464333, places=7)

    def test_calculate_2(self):
        result = calculator.calculate("2+2*2/2-2")
        self.assertAlmostEqual(float(result), 2, places=7)

    def test_calculate_3(self):
        result = calculator.calculate("(1-(-1+((-1)+(1))+(+1)-(-1)+1-(+1)))*17")
        self.assertAlmostEqual(float(result), 0, places=7)

    def test_calculate_4(self):
        result = calculator.calculate(
            "sin(0)+cos(0)+tan(0)+asin(0)+acos(0)+atan(0)")
        self.assertAlmostEqual(float(result), 2.5707963, places=7)

    def test_calculate_5(self):
        result = calculator.calculate("9mod(2)*3^2-sqrt(9)")
        self.assertAlmostEqual(float(result), 6, places=7)

    def test_calculate_6(self):
        result = calculator.calculate("ln(1)+log(100)")
        self.assertAlmostEqual(float(result), 2, places=7)

    def test_calculate_7(self):
        result = calculator.calculate("2^(-3)+14")
        self.assertAlmostEqual(float(result), 14.125, places=7)

    def test_calculate_8(self):
        result = calculator.calculate("(((2^(-3)+14)*3+2)-1*4)-(-4)")
        self.assertAlmostEqual(float(result), 44.375, places=7)

    def test_calculate_9(self):
        result = calculator.calculate("2*(3-3)")
        self.assertAlmostEqual(float(result), 0, places=7)

    def test_calculate_10(self):
        result = calculator.calculate("sqrt(1)-1/2*sin(1^2-2-4+13)")
        self.assertAlmostEqual(float(result), 0.505320876688309, places=7)

    def test_calculate_11(self):
        result = calculator.calculate("(-71)mod(-12)")
        self.assertAlmostEqual(float(result), -11, places=7)

    def test_calculate_12(self):
        result = calculator.calculate("((1.0)-2.0-((-3.0)-(4.0)))-5.0-(-6.0)")
        self.assertAlmostEqual(float(result), 7, places=7)

    def test_calculate_13(self):
        result = calculator.calculate("3+7-")
        self.assertIsNone(result)

    def test_calculate_14(self):
        result = calculator.calculate("3+sin(e+7)")
        self.assertIsNone(result)

    def test_calculate_15(self):
        result = calculator.calculate(".3+17")
        self.assertIsNone(result)

    def test_calculate_16(self):
        result = calculator.calculate("(1+2)17")
        self.assertIsNone(result)

    def test_calculate_17(self):
        result = calculator.calculate("(1+2)x")
        self.assertIsNone(result)

    def test_calculate_18(self):
        result = calculator.calculate("(1++2)")
        self.assertIsNone(result)

    def test_calculate_19(self):
        result = calculator.calculate("*3")
        self.assertIsNone(result)

    def test_calculate_20(self):
        result = calculator.calculate("3*mod")
        self.assertIsNone(result)

    def test_graph_calculate_21(self):
        result = calculator.graph_calculate("sin(x)", "-10.5", "134")
        self.assertEqual(float(result[0][0]), -10.5)
        self.assertEqual(float(result[1][0]), 0.8796957599716702)

    def test_graph_calculate_22(self):
        result = calculator.graph_calculate("sin(x)))--/", "-10.5", "134")
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
