import settings
import torndb

config = settings.db
db = torndb.Connection(config['host'], config['database'], config['user'], config['password'])
