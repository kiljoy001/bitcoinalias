import base58

class Checker:
    def __init__(self, address):
        self.bitcoin_address = address

    def check_address(self):
        
        try:
            base58.b58decode_check(self.bitcoin_address)
            return True
        
        except ValueError as e:
            print(e)
            return False