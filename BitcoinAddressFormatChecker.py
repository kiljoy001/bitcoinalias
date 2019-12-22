from hashlib import sha256


class Checker:
    base58_Char = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

    def __init__(self, address):
        self.Bitcoin_Address = address
        self.Length = address.length()

    def decode_base58(self):
        n = 0
        for char in self.Bitcoin_Address:
            n = n * 58 + Checker.basee58_char.index(char)
        return n.to_bytes(self.Length, 'big')

    def check_address(self):
        try:
            address_bytes = self.decode_base58(self.Bitcoin_Address, self.Length)
            return address_bytes[-4:] == sha256(sha256(address_bytes[:-4]).digest()).digest()[:4]
        except ValueError:
            return False
