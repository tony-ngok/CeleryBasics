# 异步处理任务

from celery import group
from tasks import * # 引进所有任务

if __name__ == '__main__':
    N = 1000
    
    print("START\n")

    # 创建任务组
    add_group = group(add.s(i, 1) for i in range(N))
    mult_group = group(mult.s(i, i) for i in range(N))
    text_group = group(text.s(f"Text msg {i}") for i in range(N))

    # adds = list()
    # mults = list()
    # texts = list()

    # 异步发送任务给消息仲介：每种任务发送给各自的任务队列
    # for x in range(10):
    #     adds.append(add.apply_async((x, 1), queue='add_queue'))
    #     mults.append(mult.apply_async((x, x), queue='mult_queue'))
    #     texts.append(text.apply_async((f"Text msg {x}",), queue='text_queue'))
    adds = add_group.apply_async(queue='add_queue')
    print("SENT: adds")
    mults = mult_group.apply_async(queue='mult_queue')
    print("SENT: mults")
    texts = text_group.apply_async(queue='text_queue')
    print("SENT: texts")
    
    # 等待所有任务完成
    adds.join()
    print("DONE: adds")
    mults.join()
    print("DONE: mults")
    texts.join()
    print("DONE: texts\n")

    # 获取每个任务的结果
    for i in range(N):
        print(f"Task ID: {adds[i].id}, Result={adds[i].get(timeout=10)}")
        print(f"Task ID: {mults[i].id}, Result={mults[i].get(timeout=10)}")
        print(f"Task ID: {texts[i].id}, Result={texts[i].get(timeout=10)}\n")
    
    print("ALL DONE")