# 异步处理任务

from time import sleep
from tasks import * # 引进所有任务

if __name__ == '__main__':
    for y in range(10):
        print(f"Tasks {y} begin\n")

        adds = list()
        mults = list()
        texts = list()

        # 异步发送任务给消息仲介
        for x in range(10):
            adds.append(add.delay(x, y))
            mults.append(mult.delay(x, y))
            texts.append(text.delay(f"x={x} y={y}"))
        
        print(f"Tasks {y} sent\n")

        # while adds[0].state == 'PENDING':
        #     p = text.delay("pending...")
        #     print(p.get(timeout=1))

        # 获取每个任务的结果
        for i in range(10):
            print(f"Task ID: {adds[i].id}, Result={adds[i].get(timeout=3)}")
            print(f"Task ID: {mults[i].id}, Result={mults[i].get(timeout=3)}")
            print(f"Task ID: {texts[i].id}, Result={texts[i].get(timeout=3)}")
            print()
        
        print(f"Tasks {y} end")