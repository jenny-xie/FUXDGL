import time
from pymongo import MongoClient
from flask import Flask

server = Flask(__name__)

client = MongoClient('mongodb+srv://user:user123@cluster0.rjmqv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client['database']
col = db['transcripts']

@server.route('/')
def index():
    return 'INDEX'

@server.route('/time')
def get_current_time():
    return {'time':time.time()}

@server.route('/test')
def test():
    mydict = { "name": "John", "address": "Highway 37" }
    db.col.insert_one(mydict)
    return 'Hello, World!'

if __name__ == '__main__':
    server.run()