# 调度任务

from celery import group
from tasks import lookup_id

if __name__ == '__main__':
    key = input("Input '1': ")
    passcode = input("Input 'lookup.php': ")

    id_input = input("Input id: ")
    id = int(id_input) if id_input.isdigit() else 0

    # 模拟长时间任务
    time_input = input("Sleep secondes (default 0): ")
    time = int(time_input) if time_input.isdigit() else 0

    # https://stackoverflow.com/questions/64310225/wait-for-all-tasks-in-a-celery-group-to-finish-or-error-out
    tasks_sig = group(lookup_id.s(key, passcode, id+i, time+i) for i in range(10)) # 生成一组任务签名（为了能够async）
    tasks = tasks_sig.apply_async() # 生成一个GroupResult（ResultSet），等待所有任务都结束
    results = tasks.get(propagate=False) # 相当于使用.join()以结束异步处理

    # print("Tasks ready")
    # print("Failed?", tasks.failed()) # 检查是否有任务失败
    
    for i in range(len(results)):
        print("i:", results[i])
        # print("i:", results[i].traceback)
        print()