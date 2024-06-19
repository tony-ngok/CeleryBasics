# 配置celery

from celery import Celery

# 消息代理仲介使用localhost数据库0
# 后端使用使用localhost数据库1
app = Celery('proj1',
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/1')

# 这个字典指明哪个任务会被发送到哪个队列中
app.conf.update(
    task_routes={
        'tasks.add': {'queue': 'add'}, # add任务发送到add队列中
        'tasks.mult': {'queue': 'mult'},
        'tasks.text': {'queue': 'text'},
    },
)