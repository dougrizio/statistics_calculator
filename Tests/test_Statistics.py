import csv
import unittest
from Stats.Statistics import Statistics
from Calc.Addition import addition
from Calc.Subtraction import subtraction
from Calc.Division import division
from pprint import pprint

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

        # POTENTIAL CHANGES
            # use random number generator to populate csv?
            # combine data into a single file
            # create separate csv reader

            # may also be able to use:
                # dataset = list(test_mean_data)
                # print(dataset[1])

    def test_simple_sample(self):

        print("-------------Simple Sample Test--------------")
        test_sample_data = MyTestCase.CsvReader('/Tests/Data/ut_mean1.csv')

        data = []

        for row in test_sample_data:
            data.append(row['Value'])
        self.assertEqual(len(self.statistics.get_simple_sample(data)), 6 )



    def test_median(self):
        test_median_data = MyTestCase.CsvReader('/Tests/Data/ut_numbers.csv')
        data = []
        for row in test_median_data:
            data.append(float(row['Value']))
        data_slice = data[0:100]
        print(self.statistics.get_median(data_slice))


    #def test_median(self):
        #test_median_data = [line for line in (MyTestCase.CsvReader('/Tests/Data/ut_floats.csv'))]
        #for line in test_median_data:
            #numbers = [float(x) for x in line]
            #sum = 0
            #for number in numbers:
                #sum = sum + number
            #print(numbers)
            #print("The sum of numbers is: ", sum)

    #def test_median(self):
        #test_median_data = MyTestCase.CsvReader('/Tests/Data/ut_numbers.csv')
        #data = []
        #for row in test_median_data:
            #data.extend(float(row['Value']))
            #print(self.statistics.get_median(data))

if __name__ == '__main__':
    unittest.main()