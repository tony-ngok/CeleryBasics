# 调度任务

from celery import group
from tasks import lookup_id

# 回调检查任务是否成功
# def callback(result):
#     if result.successful():
#         print('SUCCESS')
#         print(result.result)
#     elif result.failed():
#         print('FAILURE:')
#         print(result.traceback)
#     else:
#         print("State:", result.state)

if __name__ == '__main__':
    key = input("Input '1': ")
    passcode = input("Input 'lookup.php': ")

    id_input = input("Input id: ")
    id = int(id_input) if id_input.isdigit() else 0

    # 模拟长时间任务
    time_input = input("Sleep secondes (default 0): ")
    time = int(time_input) if time_input.isdigit() else 0

    # result = lookup_id.delay(time, url)
    # print(url)

    # https://stackoverflow.com/questions/64310225/wait-for-all-tasks-in-a-celery-group-to-finish-or-error-out
    tasks_sig = group(lookup_id.s(key, passcode, id+i, time+i) for i in range(10)) # 生成一组任务签名（为了能够async）
    tasks = tasks_sig.apply_async() # 生成一个GroupResult（ResultSet），等待所有任务都结束
    results = tasks.get(propagate=False) # 相当于使用.join()以结束异步处理
    
    for i in len(results):
        print("i:", results[i])
        # print("i:", results[i].traceback)
        print()
    