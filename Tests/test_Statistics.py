import csv
import unittest
from Stats.Statistics import Statistics
from pprint import pprint

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_results_property(self):
        self.assertEqual(self.statistics.result, 0)

    def test_mean(self):
        test_mean_data = MyTestCase.CsvReader('/Tests/Data/ut_mean1.csv')
        test_mean_answer = MyTestCase.CsvReader('/Tests/Data/ut_mean2.csv')
        data = []
        for row in test_mean_data:
            data.append(float(row['Value']))
        for row in test_mean_answer:
            answer = float(row['Value 1'])
            self.assertEqual(self.statistics.get_mean(data), answer)
            self.assertEqual(self.statistics.result, float(row['Value 1']))

        # POTENTIAL CHANGES
            # use random number generator to populate csv?
            # combine data into a single file
            # create separate csv reader

            # may also be able to use:
                # dataset = list(test_mean_data)
                # print(dataset[1])

    def test_simple_sample(self):
        test_sample_data = MyTestCase.CsvReader('/Tests/Data/ut_mean1.csv')

        data = []
        for row in test_sample_data:
            data.append(float(row['Value 1']))
        self.assertEqual(len(self.statistics.get_simple_sample(data)), 5 )



    @staticmethod
    def CsvReader(filepath):
        data = []
        with open(filepath) as text_data:
            csv_data = csv.DictReader(text_data, delimiter=',')
            for row in csv_data:
                data.append(row)
        return data

if __name__ == '__main__':
    unittest.main()