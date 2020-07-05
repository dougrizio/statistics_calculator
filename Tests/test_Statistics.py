import csv
import unittest
from Stats.Statistics import Statistics
from collections import Counter

from Calc.Addition import addition
from Calc.Subtraction import subtraction
from Calc.Multiplication import multiplication
from Calc.Division import division
from Calc.Squaring import squaring
from Calc.Squarerooting import squarerooting

from Stats.RandomGenerators import list_generator
from Calc.Calculator import Calculator

class MyTestCase(unittest.TestCase):

    @staticmethod
    def CsvReader(filepath):
        data = []
        with open(filepath) as text_data:
            csv_data = csv.DictReader(text_data, delimiter=',')
            for row in csv_data:
                data.append(row)
        return data

    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_results_property(self):
        self.assertEqual(self.statistics.result, 0)
       
        # POTENTIAL CHANGES
            # use random number generator to populate csv?
            # combine data into a single file
            # create separate csv reader

            # may also be able to use:
                # dataset = list(test_data)
                # print(dataset[1])

    def test_mean(self):
        test_mean_data = MyTestCase.CsvReader('/Tests/Data/ut_numbers.csv')
        test_mean_answer = MyTestCase.CsvReader('/Tests/Data/ut_answers.csv')
        data = []
        for row in test_mean_data:
            data.append(float(row['Value']))
        for row in test_mean_answer:
            answer = float(row['Mean'])
            self.assertEqual(self.statistics.get_mean(data), answer)
            self.assertEqual(self.statistics.result, float(row['Mean']))

    def test_median(self):
        test_median_data = MyTestCase.CsvReader('/Tests/Data/ut_numbers.csv')
        test_median_answer = MyTestCase.CsvReader('/Tests/Data/ut_answers.csv')
        data = []
        for row in test_median_data:
            data.append(float(row['Value']))
        data_slice = data[0:100]
        for row in test_median_answer:
            answer = float(row['Median'])
            self.assertEqual(self.statistics.get_median(data_slice), answer)
            self.assertEqual(self.statistics.result, float(row['Median']))

    def test_mode(self):
        test_mode_data = MyTestCase.CsvReader('/Tests/Data/ut_mode.csv')
        test_mode_answer = MyTestCase.CsvReader('/Tests/Data/ut_answers.csv')
        data = []
        for row in test_mode_data:
            data.append(float(row['Value']))
        data_slice = data[0:11]
        for row in test_mode_answer:
            answer = float(row['Mode'])
            self.assertEqual(self.statistics.get_mode(data_slice), answer)
            self.assertEqual(self.statistics.result, float(row['Mode']))

    def test_simple_sample(self):

        print("-------------Simple Sample Test--------------")
        test_sample_data = MyTestCase.CsvReader('/Tests/Data/ut_numbers.csv')

        data = []

        for row in test_sample_data:
            data.append(row['Value'])
        self.assertEqual(len(self.statistics.get_simple_sample(data)), 6 )

    def test_confidence_interval(self):
        # for testing
        population = [1, 5, 9, 5, 3, 1, 8, 8]
        # sample = list_generator(seed = 0, decimal = 0)
        self.result = self.statistics.get_confidence_interval(population)
        print("------CI Test------")
        self.assertEqual(len(self.result), 2)
        self.assertEqual(self.result[0], 2.471007117447738)
        self.assertEqual(self.result[1], 7.528992882552262)

    def test_margin_of_error(self):

        test_me_data = MyTestCase.CsvReader('/Tests/Data/ut_multiplication.csv')
        print("----ME test----")
        for row in test_me_data:
            self.result = self.statistics.get_margin_of_error(row['Value 1'], row['Value 2'])
            self.assertEqual(self.result, float(row['Result']))
            print(self.result)

    # needs work calculations taken from library will
    def test_cochran(self):
        n1 = 100000
        cl1 = 0.95
        e1 = 0.05
        p1 = 0.5

        self.result = self.statistics.get_cochrans_sample(n1, cl1, e1, p1)

        self.assertEqual(self.result, 383)







if __name__ == '__main__':
    unittest.main()