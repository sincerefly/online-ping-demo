#!/bin/env python
# -*- coding: utf-8 -*-
from flask import copy_current_request_context
from flask_socketio import SocketIO, emit
from subprocess import Popen, PIPE
from threading import Thread
from flask import Flask
import eventlet
eventlet.monkey_patch()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode='eventlet')


@socketio.on('ping_request', namespace='/test')
def ping_message(message):
     
    @copy_current_request_context
    def background_thread(url):
        
        # 设置ping的次数
        cmd = 'ping -c 6 ' + url
        r = Popen(cmd, shell=True, stdout=PIPE)
        for line in iter(r.stdout.readline, b''):
            line = line.strip('\r\n')
            print line
            emit('ping_response', {'data': line}, namespace='/test')

    url = message['url']
    thread = Thread(target=background_thread, args=(url, ))
    thread.daemon = True
    thread.start()

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0')





