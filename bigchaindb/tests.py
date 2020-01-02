from django.test import TestCase, SimpleTestCase
from .BitcoinAddressFormatChecker import Checker

class Test_Bitcoin_Address_Format_Checker(SimpleTestCase):
    Checker = Checker()

    def setUp(self):
        self.GoodAddress = '18V6RzeJ6wodhyQNAwrCdRD7mAUavggWkZ'
        self.BadChecksum = '17V6RzeJ6wodhyQNAwrCdRD7mAUavggWkZ'
        self.BadTooFewChar ='6RzeJ6wodhyQN'
        return super().setUp()
        
    def tearDown(self):
        Test_Bitcoin_Address_Format_Checker.Checker = Checker()
        return super().tearDown()

    def test_good_address_returns_true(self):
        Test_Bitcoin_Address_Format_Checker.Checker.update_address(self.GoodAddress)
        self.assertTrue(Test_Bitcoin_Address_Format_Checker.Checker.check_address())
    
    def test_bad_checksum_returns_false(self):
        Test_Bitcoin_Address_Format_Checker.Checker.update_address(self.BadChecksum)
        self.assertFalse(Test_Bitcoin_Address_Format_Checker.Checker.check_address())

    def test_too_few_characters_returns_false(self):
        Test_Bitcoin_Address_Format_Checker.Checker.update_address(self.BadChecksum)
        self.assertFalse(Test_Bitcoin_Address_Format_Checker.Checker.check_address())