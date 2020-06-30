import unittest
import Calc.RandomGenerators

class MyTestCase(unittest.TestCase):
    def test_something(self):
        #List evaluates to False if empty
        test_list = Calc.RandomGenerators.list_generator(2)

        self.assertTrue(test_list)

    def test_random_item(self):
        #test default list count
        test_list = Calc.RandomGenerators.list_generator(2)
        self.assertEqual(len(test_list), 100)



if __name__ == '__main__':
    unittest.main()
