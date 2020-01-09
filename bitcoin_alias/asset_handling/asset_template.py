from bigchaindb_driver import BigchainDB
from bitcoin_alias.asset_handling.create_user import User

"""Test Keys: Public:'7JxiZgoRUZvASFZQbgNbGjjqPHhJQTDKeeyyueMp4rjC', Private: 'B6uFt3PJNHhK48jE6m24j5mu2ykEjHyVKV4CpWUuFxp9'"""

class Asset:
    """sets and describes json template for BigChainDb asset"""

    URL = 'https://test.ipdb.io/'
    Bdb = BigchainDB(URL)

    def __init__(self, User):
        self.User = User
        self.bitcoin_address_asset_data = {
            'data': {
                'address_alias_pair': {
                    'bitcoin_address': self.User.BitcoinAddress,
                    }
                }
            }

    def transfer_asset(self, public_key, owners_private_key, txid, new_alias = None):
        """Update asset with new alias"""
        creation_tx = Asset.Bdb.transactions.retrieve(txid)
        asset_id = creation_tx['id']
        transfer_asset = {
            'id': asset_id
        }
        """Check if alias is being updated"""
        if new_alias is None:
            metadata = creation_tx['metadata']
        else:
            metadata = {'updated_alias':new_alias}
        
        """Transfer Data"""
        output_index = 0
        output = creation_tx['outputs'][output_index]
        transfer_input = {
            'fulfillment': output['condition']['details'],
            'fulfills': {
            'output_index': output_index,
            'transaction_id': creation_tx['id'],
            },
            'owners_before': output['public_keys'],
            }

        prepared_transfer_tx = Asset.Bdb.transactions.prepare(
            operation='TRANSFER',
            asset=transfer_asset,
            inputs=transfer_input,
            recipients=public_key,
            metadata=metadata,
        )

        """Sign transaction"""
        fulfilled_transfer_tx = Asset.Bdb.transactions.fulfill(
            prepared_transfer_tx,
            private_keys = owners_private_key
        )

        """Send to node"""
        Asset.Bdb.transactions.send_commit(fulfilled_transfer_tx)

    def create_asset(self):
        """Create an asset"""
        prepared_creation_tx = Asset.Bdb.transactions.prepare(
            operation='CREATE',
            signers=self.User.KeyPair.public_key,
            asset=self.bitcoin_address_asset_data,
            metadata={'updated_alias':self.User.Alias}
        )

        """Sign transaction with private key"""
        signed_transaction = Asset.Bdb.transactions.fulfill(
            prepared_creation_tx,
            private_keys=self.User.KeyPair.private_key
        )

        """Send transaction to BigchainDb node"""
        sent_token = Asset.Bdb.transactions.send_commit(signed_transaction)

        """Return TxId"""
        return sent_token['id']