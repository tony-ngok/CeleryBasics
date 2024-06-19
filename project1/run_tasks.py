# 异步处理任务

from tasks import * # 引进所有任务

if __name__ == '__main__':
    print("START")
    
    adds = list()
    mults = list()
    texts = list()

    # 异步发送任务给消息仲介：每种任务发送给各自的任务队列
    for x in range(10):
        adds.append(add.apply_async((x, 1), queue='add_queue'))
        mults.append(mult.apply_async((x, x), queue='mult_queue'))
        texts.append(text.apply_async((f"Text msg {x}",), queue='text_queue'))
    
    print("ALL TASKS SENT\n")

    # 获取每个任务的结果
    for i in range(10):
        print(f"Task ID: {adds[i].id}, Result={adds[i].get(timeout=10)}")
        print(f"Task ID: {mults[i].id}, Result={mults[i].get(timeout=10)}")
        print(f"Task ID: {texts[i].id}, Result={texts[i].get(timeout=10)}")
        print()