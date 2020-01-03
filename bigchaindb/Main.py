from CreateUser import User
from AssetTemplate import Asset

new_asset = Asset('18V6RzeJ6wodhyQNAwrCdRD7mAUavggWkZ', 'scott.j.guyton')
#new_asset.create_asset('7JxiZgoRUZvASFZQbgNbGjjqPHhJQTDKeeyyueMp4rjC', 'B6uFt3PJNHhK48jE6m24j5mu2ykEjHyVKV4CpWUuFxp9')
print(new_asset.Bdb.metadata.get(search='scott.j.guyton'))
