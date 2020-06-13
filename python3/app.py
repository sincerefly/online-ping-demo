#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import copy_current_request_context, send_from_directory
from flask_socketio import SocketIO, emit
from eventlet.green import subprocess
from eventlet.green import threading
from flask import Flask
import os

DIST_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../dist')

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode='eventlet')

@app.route('/', methods=['GET'])
def serve_dir_directory_index():
    return send_from_directory(DIST_DIR, 'index.html')

@app.route('/<path:path>', methods=['GET'])
def serve_file_in_dir(path):
    return send_from_directory(DIST_DIR, path)

@socketio.on('ping_request', namespace='/test')
def ping_message(message):

    @copy_current_request_context
    def background_thread(addr):

        cmd = 'ping -c 6 {}'.format(addr)
        r = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        for line in iter(r.stdout.readline, b''):
            line = str(line).strip('\r\n')
            print(line)
            emit('ping_response', {'data': str(line)}, namespace='/test')

    addr = message['url']
    thread = threading.Thread(target=background_thread, args=(addr, ))
    thread.daemon = True
    thread.start()

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0')


