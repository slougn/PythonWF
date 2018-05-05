import unittest
from city_functions import city_functions
# print(city_functions('handan','china'))
class CityTestCase(unittest.TestCase):
    """测试city_function的功能"""
    def test_cities(self):
        formatted = city_functions('handan','china')
        self.assertEqual(formatted,'Handan China')

unittest.main

