import time
import json
from gridfs import GridFS
from pymongo import MongoClient
from flask import Flask, make_response
from flask import request, render_template, send_file, redirect, url_for
from Parser import splice
import os

server = Flask(__name__)

server.config['UPLOAD_PATH'] = 'uploads'

client = MongoClient('mongodb+srv://user:user123@cluster0.rjmqv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client['database']
col = db['transcripts']
grid_fs = GridFS(db)

@server.route('/uploadvid/', methods=['POST'])
def uploadvid():
    #local copy
    video_file = request.files['video']
    
    if video_file.filename != '':
        video_file.save(os.path.join(server.config['UPLOAD_PATH'],'recording.mp4'))
    

    # with grid_fs.new_file(filename='recording.mp4') as fp:
    #     fp.write(request.data)
    #     file_id = fp._id

    # if grid_fs.find_one(file_id) is not None:
    #     return json.dumps({'status': 'File saved successfully'}), 200
    # else:
    #     return json.dumps({'status': 'Error occurred while saving file.'}), 500

@server.route('/uploadtext/', methods=['POST'])
def uploadtext():
    transcript_file = request.files['transcript']
    if transcript_file.filename != '':
        transcript_file.save(os.path.join(server.config['UPLOAD_PATH'],'transcript.vtt'))
    # with grid_fs.new_file(filename='transcript.vtt') as fp:
    #     fp.write(request.data)
    #     file_id = fp._id

    # if grid_fs.find_one(file_id) is not None:
    #     return json.dumps({'status': 'File saved successfully'}), 200
    # else:
    #     return json.dumps({'status': 'Error occurred while saving file.'}), 500

@server.route('/splice/', methods=['POST'])
def parse():
    fields = request.get_json().get('fields')
    startword = fields["start"]
    stopword = fields["stop"]
    splice(startword, stopword)
    if grid_fs.find_one('splice.mp4') is not None:
        return json.dumps({'status': 'File saved successfully'}), 200
    else:
        return json.dumps({'status': 'Error occurred while saving file.'}), 500

@server.route('/download/')
def retrieve():
    grid_fs_file = grid_fs.find_one({'filename': splice.mp4})
    response = make_response(grid_fs_file.read())
    response.headers['Content-Type'] = 'application/octet-stream'
    response.headers["Content-Disposition"] = "attachment; filename={}".format(file_name)
    return response

@server.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['video']
        uploaded_file2 = request.files['transcript']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join(server.config['UPLOAD_PATH'],'recording.mp4'))
        if uploaded_file2.filename != '':
            uploaded_file2.save(os.path.join(server.config['UPLOAD_PATH'],'transcript.vtt'))
        return redirect(url_for('index'))
    return render_template('index.html')

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