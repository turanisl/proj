import unittest
import calculator


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(1, 2), 3)

    def test_sub(self):
        self.assertEqual(calculator.sub(5, 3), 2)

    def test_mul(self):
        self.assertEqual(calculator.mul(2, 3), 6)

    def test_div(self):
        self.assertEqual(calculator.div(10, 2), 5)

    def test_div_zero(self):
        with self.assertRaises(ValueError):
            calculator.div(1, 0)


if __name__ == "__main__":
    unittest.main()
