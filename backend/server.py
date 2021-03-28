import time
from flask import Flask

server = Flask(__name__)

@server.route('/')
def index():
    return 'INDEX'

@server.route('/time')
def get_current_time():
    return {'time':time.time()}

if __name__ == '__main__':
    server.run()