from flask import Flask
from sql_tools import show_table 

app = Flask(__name__)

@app.route("/")
def testtest():
    lst = show_table()[0][1]
    #return lst
    return """
    <h1>Hello heroku</h1>
    <p>Song {song}.</p>

    """.format(song=lst)

if __name__ == '__main__':
	app.run()
