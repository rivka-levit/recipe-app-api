"""
Sample tests
"""
from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Test adding numbers together"""
        res = calc.add(2, 3)

        self.assertEquals(res, 5)

    def test_subtract_numbers(self):
        """Tests subtracting numbers from each other"""
        res = calc.subtract(5, 2)

        self.assertEquals(res, 3)
