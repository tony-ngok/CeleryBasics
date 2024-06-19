# CeleryBasics

## 针对Windows作业系统的特别工作 ##

[预先在Windows上下载并运行Redis伺服器](https://stackoverflow.com/questions/59532504/error-while-starting-celery-worker-on-django-error-10061-no-connection-could-be)：<br/>
下载并解压https://github.com/MSOpenTech/redis/releases/download/win-3.2.100/Redis-x64-3.2.100.zip <br/>
每次执行Celery worker之前，先运行redis-server.exe

[在Windows上执行Celery worker](https://stackoverflow.com/questions/59927934/valueerror-not-enough-values-to-unpack-expected-3-got-0-when-starting-celery)：<br/>
pip install gevent <br/>
-A <module名称> worker -l info -P gevent


## getting_started ##


## project1 ##

