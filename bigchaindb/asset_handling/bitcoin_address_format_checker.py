import base58

class Checker:
    """Create checker, address optional if need to be reused"""
    def __init__(self, address = None):
        self.bitcoin_address = address

    def check_address(self):
        """Checks address if it decodes correctly"""    
        try:
            base58.b58decode_check(self.bitcoin_address)
            return True
        
        except ValueError:
            #print(e)
            return False

    def update_address(self, address):
        """Updates property with a new address"""
        self.bitcoin_address = address
