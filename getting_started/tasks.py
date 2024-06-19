# Client (message/task producer)

from celery import Celery

app = Celery('tasks', broker='redis://localhost', backend='redis://localhost')

@app.task
def add(x, y):
    return x + y

@app.task
def hallo():
    return "Salut!"