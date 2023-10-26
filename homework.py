import unittest
from bracket_check import bracket_check


class MyTestCase(unittest.TestCase):
    def test_no_error(self):
        test_string = '[{(Hello)}]'
        isError, location = bracket_check(test_string)
        self.assertEqual(isError, False)
        print('Error:{isError}')
        print('location_5:', location)
        print('Chanakun Maneenai')


    def test_error_1(self):
        test_string = '[{(Hello})]'
        isError, location = bracket_check(test_string)
        self.assertEqual(isError, True)
        print('Error:{isError}')
        print('location_1:', location)

    def test_error_2(self):
        test_string = '[{(Hello'
        isError, location = bracket_check(test_string)
        self.assertEqual(isError, True)
        print('Error:{isError}')
        print('location_2:', location)

    def test_error_3(self):
        test_string = 'Hello)('
        isError, location = bracket_check(test_string)
        self.assertEqual(isError, True)
        print('Error:{isError}')
        print('location_3:', location)

    def test_error_4(self):
        test_string = '{}{'
        isError, location = bracket_check(test_string)
        self.assertEqual(isError, True)
        print('Error:{isError}')
        print('location_4:', location)




