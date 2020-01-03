from bigchaindb_driver import BigchainDB


class Asset:
    """sets and describes json template for BigChainDb asset"""

    URL = 'https://test.ipdb.io/'
    Bdb = BigchainDB(URL)

    def __init__(self, address, alias):
        self.Bitcoin_Address = address
        self.Metadata = alias
        self.Bitcoin_Address_Asset_Data = {
            'data': {
                'address_alias_pair': {
                    'bitcoin_address': self.Bitcoin_Address,
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

    def create_asset(self, public_key, owners_private_key):
        """Create an asset"""
        prepared_creation_tx = Asset.Bdb.transactions.prepare(
            operation='CREATE',
            signers=public_key,
            asset=self.Bitcoin_Address_Asset_Data,
            metadata={'updated_alias':self.Metadata}
        )

        """Sign transaction with private key"""
        signed_transaction = Asset.Bdb.transactions.fulfill(
            prepared_creation_tx,
            private_keys=owners_private_key
        )
        """Send transaction to BigchainDb node"""
        Asset.Bdb.transactions.send_commit(signed_transaction)