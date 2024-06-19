# 配置celery

from celery import Celery

# 消息代理仲介使用localhost数据库0
# 后端使用使用localhost数据库1
app = Celery('proj1',
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/1')

# 这个字典指明哪个任务会被发送（route）到哪个任务队列（默认只有“celery”）中
app.conf.update(
    task_routes={
        'tasks.add': {'queue': 'add_queue'}, # add任务发送到add队列中
        'tasks.mult': {'queue': 'mult_queue'},
        'tasks.text': {'queue': 'text_queue'},
    },

    # 需要自己定义任务队列，不然运行时没有这些队列，会发生超时错误
    task_queues={
        'add_queue': {
            'exchange': 'add_exchange',
            'binding_key': 'add',
        },
        'mult_queue': {
            'exchange': 'mult_exchange',
            'binding_key': 'mult',
        },
        'text_queue': {
            'exchange': 'text_exchange',
            'binding_key': 'text',
        },
    }
)
