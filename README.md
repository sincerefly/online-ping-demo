# online-ping-demo
一个使用Flask和SocketIO编写的网页ping工具


### Usage

下载并安装依赖

```shell
git clone git@github.com:sincerefly/online-ping-demo.git
cd online-ping-demo
pip install -r requirements.txt
```

### Run

开启两个终端来运行

```shell
python app.py

python -m SimpleHTTPServer
```

### Note

- *Flask 程序默认监听的5000端口，python 默认HTTP服务器监听的8000 端口， 请确保这两个端口没有被占用*
- *index.html并不要求和app.py放在一处，app.py只是一个接口*


打开浏览器访问（如果是本地的话）

http://localhost:8000 


![ping](https://ishell-imgs.b0.upaiyun.com/github/ping_small.gif)




