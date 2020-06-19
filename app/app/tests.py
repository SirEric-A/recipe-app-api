from django.test import TestCase
from app.calc import add,subtract


class CalcTest(TestCase):

    def test_add_numbers(self):
        """test taht two numbers are added together"""
        self.assertEqual(add(3,8),11)

    def test_subtract_numbers(slef):
        """test that values are subtracted and returned"""
        slef.assertEqual(subtract(11,5),6)