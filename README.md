# CeleryBasics

Celery是一种分布式任务队列。

## 準備工作

1. 首先在Windows电脑上安装WSL（Linux），然后使用```bash```命令进入WSL

2. [在WSL中安装pip（Python包裹管理器）](https://askubuntu.com/questions/1384406/unable-to-install-pip-into-wsl-ubuntu)：
    ```
    sudo apt-get update
    ```
    ```
    sudo apt install python3-pip
    ```

3. [安装并起用redis-server](https://stackoverflow.com/questions/36088409/error-111-connecting-to-localhost6379-connection-refused-django-heroku)：
    ```
    sudo apt-get install redis-server
    ```
    ```
    sudo service redis-server start
    ```

4. 用pip安装celery与redis的组合：
    ```
    pip install -U "celery[redis]"
    ```


## getting_started

这是一个很简单的小程式，只有两个任务，用来测试部署celery：

1. 在一个运行WSL的命令提示窗中，[执行Celery收信端（worker）](https://stackoverflow.com/questions/70618461/zsh-command-not-found-celery)以监听任务：
    ```
    python3 -m celery -A tasks worker --loglevel=INFO
    ```
    这样会显示```tasks```发信端（client）中所有celery任务：
    ```
    [tasks] 
        . tasks.add 
        . tasks.hallo
    ```
    以下一行字说明连结redis消息代理（broker）成功了：
    ```
    [INFO/MainProcess] Connected to redis://localhost:6379//
    ```

2. 打开另一个命令提示窗并运行WSL，用Python创建任务：
    ```
    python3 runs.py
    ```
    这里的两个任务按```.delay()```的顺序被异步发送；每个任务发送后，相应的```ready()```状态由False变为True。


## project1

另一个小程式，展示怎样异步创建、接受、分发并监听多个任务。

1. 本程式包含3种不同任务，分别对应3个不同的任务队列：```add_queue```、```mult_queue```、```text_queue```。
    ```
    -------------- [queues]
                .> add_queue        exchange=add_exchange(direct) key=add
                .> mult_queue       exchange=mult_exchange(direct) key=mult
                .> text_queue       exchange=text_exchange(direct) key=text
    ```

2. 本程式将任务异步发送给不同的任务队列（因此不会阻塞程式运行），然后稍后获取每个任务的结果。

3. 可打开多个运行WSL的命令提示窗；每个窗中用以下命令分别监视不同的任务队列：
    ```
    python3 -m celery -A tasks worker -Q <队列名> --loglevel=INFO
    ```