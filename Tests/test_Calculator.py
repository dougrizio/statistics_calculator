import csv
import unittest
from Calc.Calculator import Calculator
from pprint import pprint

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)

    def test_addition(self):
        test_addition_data = MyTestCase.CsvReader('/Tests/Data/ut_addition.csv')
        pprint(test_addition_data)
        for row in test_addition_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_subtraction(self):
        test_subtraction_data = MyTestCase.CsvReader('/Tests/Data/ut_subtraction.csv')
        pprint(test_subtraction_data)
        for row in test_subtraction_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_multiplication(self):
        test_multiplication_data = MyTestCase.CsvReader('/Tests/Data/ut_multiplication.csv')
        pprint(test_multiplication_data)
        for row in test_multiplication_data:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_division(self):
        test_division_data = MyTestCase.CsvReader('/Tests/Data/ut_division.csv')
        pprint(test_division_data)
        for row in test_division_data:
            self.assertAlmostEqual(self.calculator.divide(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertAlmostEqual(self.calculator.result, float(row['Result']))

    def test_squaring(self):
        test_squaring_data = MyTestCase.CsvReader('/Tests/Data/ut_squaring.csv')
        pprint(test_squaring_data)
        for row in test_squaring_data:
            self.assertEqual(self.calculator.square(row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_squarerooting(self):
        test_squarerooting_data = MyTestCase.CsvReader('/Tests/Data/ut_squarerooting.csv')
        pprint(test_squarerooting_data)
        for row in test_squarerooting_data:
            self.assertAlmostEqual(self.calculator.squareroot((row['Value 1'])), float(row['Result']))
            self.assertAlmostEqual(self.calculator.result, float(row['Result']))

    @staticmethod
    def CsvReader(filepath):
        rows = []
        with open(filepath) as text_data:
            csv_data = csv.DictReader(text_data, delimiter=',')
            for row in csv_data:
                rows.append(row)
        return rows

if __name__ == '__main__':
    unittest.main()