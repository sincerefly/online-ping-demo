const express = require('express')
const app = require('express')()
const http = require('http').Server(app)
const io = require('socket.io')(http)
const spawn = require('child_process').spawn

// 设置namespace
var nsp = io.of('/test');

const DIST_PATH = '../dist'
app.use('/', express.static(DIST_PATH))

nsp.on('connection', function(socket){

    console.log('a user connected');

    // 监听事件
    socket.on('ping_request', function(msg) {
        var child = spawn('ping', [
            '-c', '6', msg.url
        ]);

        child.stdout.setEncoding('utf8');
        child.stdout.on('data', function(chunk) {
            console.log(chunk)
            info = {
                "data": chunk
            }
            socket.emit('ping_response', info);
        });
    });
});

http.listen(5000, function() {
    console.log('listening on 0.0.0.0:5000');
});


