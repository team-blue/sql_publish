from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
import string
import random 
from flask import Flask


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
 
def add_row():
    real_new_key = key_generator()
    #songs = ('So What', 'Miles Davis', real_new_key)
    songs = ('Get Lucky', 'Daft Punk', real_new_key)
    insert_songs(songs)

def show_table():
    query = "SELECT * FROM Songs"

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
 
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        # print('Total Row(s):', cursor.rowcount)
        # for row in rows:
        #     print(row)
        return rows

    except Error as e:
        print('Error:', e)

###From Here it is FLASK#### 
# app = Flask(__name__)
# @app.route("/")
# def testtest():
#     lst = show_table()
#     return lst

 
#if __name__ == '__main__':

