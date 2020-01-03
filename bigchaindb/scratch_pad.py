from AssetTemplate import Asset

"""Just a testing spot for working with bigchaindb"""

NEW_ASSET = Asset('18V6RzeJ6wodhyQNAwrCdRD7mAUavggWkZ', 'scott.j.guyton')
TXID = NEW_ASSET.create_asset('7JxiZgoRUZvASFZQbgNbGjjqPHhJQTDKeeyyueMp4rjC', \
'B6uFt3PJNHhK48jE6m24j5mu2ykEjHyVKV4CpWUuFxp9')
print(NEW_ASSET.Bdb.metadata.get(search='scott.j.guyton') +'/n/n' + TXID)
