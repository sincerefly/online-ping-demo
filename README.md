# online-ping-demo

简易在线ping工具，将ping命令输出实时显示到web页面，基于Flask-SocketIO/socket.io

- python 版本基于(flask | Flask-SocketIO | gevent)
- nodejs 版本基于(express | socket.io)


### Usage

下载并安装依赖

```shell
git clone git@github.com:sincerefly/online-ping-demo.git
cd online-ping-demo

# python
cd python
pip install -r requirements.txt

# nodejs
cd nodejs
npm install
```

### Run

首先将静态页变为可访问

```shell
# 如使用python的简易服务器，默认会监听5000端口
python -m SimpleHTTPServer

```

```shell
# python
python app.py

# nodejs
nodejs index.js
```

### Note

- *Flask 程序默认监听的5000端口，python 默认HTTP服务器监听的8000 端口， 请确保这两个端口没有被占用*
- *index.html并不要求和app.py放在一处，app.py只是一个接口*


打开浏览器访问（如果是本地的话）

http://localhost:8000


![ping](https://ishell-imgs.b0.upaiyun.com/github/ping_small.gif)



