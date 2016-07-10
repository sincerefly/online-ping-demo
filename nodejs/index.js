var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var spawn = require('child_process').spawn;

// 设置namespace
var nsp = io.of('/test');

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






