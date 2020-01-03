from django.test import TestCase, SimpleTestCase
from bigchaindb.asset_handling.bitcoin_address_format_checker import Checker
from bigchaindb.asset_handling.asset_template import Asset
from bigchaindb_driver.crypto import generate_keypair
from bigchaindb_driver.driver import BigchainDB

class Test_Bitcoin_Address_Format_Checker(SimpleTestCase):
    Checker = Checker()

    def setUp(self):
        self.GoodAddress = '18V6RzeJ6wodhyQNAwrCdRD7mAUavggWkZ'
        self.BadChecksum = '17V6RzeJ6wodhyQNAwrCdRD7mAUavggWkZ'
        self.BadTooFewChar = '6RzeJ6wodhyQN'
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

class Test_BigchainDB_Transactions(TestCase):
    URL = 'https://test.ipdb.io/'
    Bdb = BigchainDB(URL)

    def setUp(self):
        self.bitcoin_address = '18V6RzeJ6wodhyQNAwrCdRD7mAUavggWkZ'
        self.alias = 'scott.j.guyton'
        self.key_pair = generate_keypair()
        self.asset = Asset(self.bitcoin_address, self.alias)
        self.TxId = None
        return super().setUp()
    
    def tearDown(self):
        self.alias = 'scott.j.guyton'
        self.key_pair = generate_keypair()
        return super().tearDown()
    
    def test_creation_of_asset_returns_true(self):
        self.TxId = self.asset.create_asset(self.key_pair.public_key, self.key_pair.private_key)
        self.assertTrue(len(self.asset.Bdb.metadata.get(search='scott.j.guyton')) > 0)
    
    def test_transfer_of_asset_to_another_user(self):
        new_key_pair = generate_keypair()
        self.asset.transfer_asset(new_key_pair, 'B6uFt3PJNHhK48jE6m24j5mu2ykEjHyVKV4CpWUuFxp9', '2397c560bd6a819f9094a168dd4304031fb7a6dd7a6983214ba79ba7a415750d', 'updated_string!')
        self.assertTrue(len(self.asset.Bdb.metadata.get(search='updated_string!')) > 0)