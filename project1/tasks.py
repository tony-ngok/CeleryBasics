# 定义任务

from celery_app import app

@app.task
def add(x, y):
    return x+y

@app.task
def mult(x, y):
    return x*y

@app.task
def text(txt):
    return "Text"