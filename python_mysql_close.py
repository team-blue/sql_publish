from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config 

def close_connection():
##Connect to MySQL database 

	db_config = read_db_config()

	try:
		print('Closing MySQL database...')
		conn = MySQLConnection(**db_config)
		conn.close()
		print('Connection closed.')

		
	else:
		print('closing failed.')

	except Error as error:
		print(error)
		

if __name__ == '__main__':
	close_connection()