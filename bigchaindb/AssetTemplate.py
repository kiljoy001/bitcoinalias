from bigchaindb_driver import BigchainDB


class Asset:
    """sets and describes json template for BigChainDb asset"""

    URL = 'https://test.ipdb.io/'

    def __init__(self, address, alias, user_key_pair):
        self.bdb = BigchainDB(Asset.URL)
        self.Bitcoin_Address = address
        self.Alias = alias
        self.TxId = None
        self.key_pair = user_key_pair
        self.Bitcoin_Address_Asset_Data = {'data': {
            'address_alias_pair': {
                'bitcoin_address': self.Bitcoin_Address,
                'alias_name': self.Alias
            }
        }
        }

    def append_alias_name(self, pubkey, new_alias):
        """Update asset with new alias"""
        prepared_append_tx = self.bdb.transactions.retrieve(self.TxId)
        asset_id = prepared_append_tx['id']
        transfer_asset = {
            'id': asset_id
        }
        output_index = 0
        output = prepared_append_tx['outputs']

    def create_alias_asset(self):
        """Create an asset"""
        prepared_creation_tx = self.bdb.transactions.prepare(
            operation='CREATE',
            signers=self.key_pair.public_key,
            asset=self.Bitcoin_Address_Asset_Data
        )

        """Sign transaction with private key"""
        signed_transaction = self.bdb.transactions.fulfill(
            prepared_creation_tx,
            private_keys=self.key_pair.private_key
        )
        """Send transaction to BigchainDb node"""
        send_to_bigchain = self.bdb.transactions.send_commit(signed_transaction)

        """Transaction check"""
        if send_to_bigchain == signed_transaction:
            self.TxId = signed_transaction['id']
            return True
        else:
            return False



