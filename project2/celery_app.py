# 配置celery

from celery import Celery

app = Celery('meals', broker='redis://localhost:6379/0', backend='redis://localhost:6379/1')