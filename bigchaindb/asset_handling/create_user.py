from bigchaindb_driver.crypto import generate_keypair
from bitcoin_address_format_checker import Checker


class User:

    def __init__(self):
        self.KeyPair = None
        self.BitcoinAddress = None

    def create(self):
        """Create key pair for BigChainDB using bitcoin address as seed"""
        self.KeyPair = generate_keypair()

    def show_keys(self):
        """shows keys for the user"""
        print('public key: ' + self.KeyPair.public_key + "\n" 'private key :' + self.KeyPair.private_key)

    def set_bitcoin_address(self, bitcoin_address):
        """Set the bitcoin address"""
        check_if_valid = Checker(bitcoin_address)
        if check_if_valid.check_address():
            self.BitcoinAddress = bitcoin_address
            print("Address appears to be valid." + "\n" "Address recorded.")
        else:
            print("That address doesn't look valid." + "\n" "Please enter another address.")

