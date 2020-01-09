from bigchaindb_driver.crypto import generate_keypair
from bitcoin_address_format_checker import Checker


class User:

    def __init__(self):
        self.KeyPair = None
        self.BitcoinAddress = None
        self.Alias = None

    def generate_keys(self):
        """Create key pair for BigChainDB using bitcoin address as seed"""
        if self.KeyPair is None:
            self.KeyPair = generate_keypair()
        else:
            pass

    def show_keys(self):
        """shows keys for the user"""
        #print('public key: ' + self.KeyPair.public_key + "\n" 'private key :' + self.KeyPair.private_key)
        return [self.KeyPair.public_key, self.KeyPair.private_key]

    def set_bitcoin_address_and_alias(self, alias, bitcoin_address):
        """Set the bitcoin address and alias"""
        check_if_valid = Checker(bitcoin_address)
        if check_if_valid.check_address():
            self.BitcoinAddress = bitcoin_address
            self.Alias = alias
        else:
            return ValueError
