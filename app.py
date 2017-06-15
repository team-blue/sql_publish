from flask import Flask
from sql_tools import show_table 

app = Flask(__name__)

@app.route("/")
def testtest():
    lst = show_table()
    return lst

if __name__ == '__main__':
	app.run()
