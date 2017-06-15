from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
import string
import random 

key_history = []

def key_generator(size = 10, chars = string.ascii_uppercase + string.digits):
    new_key = ''.join(random.choice(chars) for _ in range(size))
    while True:
        if new_key not in key_history:
            key_history.append(new_key)
            return str(new_key)
            break
 
def insert_songs(songs):
    new_key = key_generator()
    query = "INSERT INTO Songs(songName,musician,song_key) " \
            "VALUES(%s,%s,%s)"
 
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
 
        cursor = conn.cursor()
        cursor.execute(query,songs)
 
        conn.commit()
    except Error as e:
        print('Error:', e)
 
    finally:
        cursor.close()
        conn.close()
 
def main():
    real_new_key = key_generator()
    #songs = ('So What', 'Miles Davis', real_new_key)
    songs = ('Get Lucky', 'Daft Punk', real_new_key)
    insert_songs(songs)
 
if __name__ == '__main__':
    main()
