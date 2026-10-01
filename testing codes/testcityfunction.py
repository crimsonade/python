import unittest
from city_function import get_city

class CityTestCase(unittest.TestCase):
    """Test for 'city_function.py"""

    def test_location(self):
        f_city= get_city('kumasi', 'ghana')
        self.assertEqual(f_city, 'Kumasi, Ghana')

    def test_location_population(self):
        f_city= get_city('tamale','ghana', 500000)
        self.assertEqual(f_city, 'Tamale, Ghana-Population= 500000')
if __name__=='__main__':
    unittest.main()
                    