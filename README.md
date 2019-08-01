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
pip3 install -r requirements.txt

# nodejs
cd nodejs
npm install
```

### Run

首先将静态页变为可访问

```shell
# python
python app.py

# nodejs
nodejs index.js
```

### Note

打开浏览器访问

http://[SERVER_IP]:5000


![ping](./1.gif)



