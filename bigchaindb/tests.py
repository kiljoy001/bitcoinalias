from django.test import TestCase, SimpleTestCase
from .BitcoinAddressFormatChecker import Checker

class Test_Bitcoin_Address_Format_Checker(SimpleTestCase):
    def setUp(self):
        self.GoodAddress = '18V6RzeJ6wodhyQNAwrCdRD7mAUavggWkZ'
        self.GoodCheck = Checker(self.GoodAddress)
        return super().setUp()

    def test_good_address_returns_true(self):
        self.assertTrue(self.GoodCheck.check_address())