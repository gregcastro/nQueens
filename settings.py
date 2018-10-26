db_password = 'my_password'
db_user = 'my_user'
db_name = 'my_dbname'

try:
	from local_settings import *
except ImportError:
	pass
