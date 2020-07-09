import csv
import unittest
from Stats.Statistics import Statistics
from Stats.RandomGenerators import list_generator
import Stats.RandomGenerators
from Stats.ConfidenceInterval import confidence_interval

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

    def test_variance(self):
        test_variance_data = MyTestCase.CsvReader('/Tests/Data/ut_numbers.csv')
        test_variance_answer = MyTestCase.CsvReader('/Tests/Data/ut_answers.csv')
        data = []
        for row in test_variance_data:
            data.append(float(row['Value']))
        data_slice = data[0:100]
        for row in test_variance_answer:
            answer = float(row['Variance'])
            self.assertEqual(self.statistics.get_variance(data_slice), answer)
            self.assertEqual(self.statistics.result, float(row['Variance']))

    def test_standard_deviation(self):
        test_standard_deviation_data = MyTestCase.CsvReader('/Tests/Data/ut_numbers.csv')
        test_standard_deviation_answer = MyTestCase.CsvReader('/Tests/Data/ut_answers.csv')
        data = []
        for row in test_standard_deviation_data:
            data.append(float(row['Value']))
        data_slice = data[0:100]
        for row in test_standard_deviation_answer:
            answer = float(row['Standard_Deviation'])
            self.assertEqual(self.statistics.get_standard_deviation(data_slice), answer)
            self.assertEqual(self.statistics.result, float(row['Standard_Deviation']))

    def test_zscore(self):
        test_zscore_data = MyTestCase.CsvReader('/Tests/Data/ut_zvalues.csv')
        data = []
        for row in test_zscore_data:
            data.append(float(row['Values']))
        data_slice = data[0:10]
        answers = []
        for row in test_zscore_data:
            answers.append(float(row['ZScores']))
        self.assertEqual((self.statistics.get_zscore(data_slice)), answers)

    def test_simple_sample(self):

        test_sample_data = MyTestCase.CsvReader('/Tests/Data/ut_numbers.csv')

        data = []

        for row in test_sample_data:
            data.append(row['Value'])
        self.assertEqual(len(self.statistics.get_simple_sample(data)), 6 )

    def test_margin_of_error(self):

        test_me_data = MyTestCase.CsvReader('/Tests/Data/ut_multiplication.csv')

        for row in test_me_data:
            self.result = self.statistics.get_margin_of_error(row['Value 1'], row['Value 2'])
            self.assertEqual(self.result, float(row['Result']))


    # needs work calculations taken from library
    def test_cochran(self):
        n1 = 100000
        cl1 = 0.95
        e1 = 0.05
        p1 = 0.5

        self.result = self.statistics.get_cochrans_sample(n1, cl1, e1, p1)

        self.assertEqual(self.result, 383)

        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]


    def test_sample_ci_width(self):
        sample = list_generator(stop=10000)
        ci = confidence_interval(sample)
        confidence_val = ci[0]
        width = ci[2]
        confidence = .95
        base_percent = .5

        self.result = self.statistics.get_sample_ci_width(confidence, width)
        self.assertEqual(len(sample), 10000)

    def test_confidence_interval(self):
        # for testing
        population = [1, 5, 9, 5, 3, 1, 8, 8]
        # sample = list_generator(seed = 0, decimal = 0)
        self.result = self.statistics.get_confidence_interval(population)

        self.assertEqual(len(self.result), 3)
        self.assertEqual(self.result[0], 2.471007117447738)
        self.assertEqual(self.result[1], 7.528992882552262)

    def test_something(self):
        # List evaluates to False if empty
        test_list = Stats.RandomGenerators.list_generator()
        self.assertTrue(test_list)

    def test_random_item(self):
        # test default list count
        test_list = Stats.RandomGenerators.list_generator()
        self.assertEqual(len(test_list), 100)

    def test_random_seed(self):
        seed_val = 6
        choice = Stats.RandomGenerators.random_seed(seed=seed_val)
        self.result = seed_val
        self.assertEqual(self.result, 6)

if __name__ == '__main__':
    unittest.main()

