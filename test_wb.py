from unittest import TestCase
from wb import fizzbuzz

class TestFizzBuzz(TestCase):

    def test_div_by_15(self):
        result_1 = fizzbuzz(15)
        self.assertEqual(result_1, 'FizzBuzz')
        result_2 = fizzbuzz(30)
        self.assertEqual(result_2, 'FizzBuzz')
        self.assertEqual(fizzbuzz(60), 'FizzBuzz')

    def test_div_by_10(self):
        pass

    def test_div_by_5(self):
        self.assertEqual(fizzbuzz(25))
        self.assertEqual(fizzbuzz(5))

    def test_negative(self):
        pass

if __name__ == '__main__':
    main()


