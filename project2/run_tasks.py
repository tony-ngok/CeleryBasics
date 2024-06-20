# 调度任务

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
    id = input("Input id: ")

    # 模拟长时间任务
    time_input = input("Sleep secondes (default 0): ")
    time = int(time_input) if time_input.isdigit() else 0

    url = f"https://www.themealdb.com/api/json/v1/{key}/{passcode}?i={id}"

    result = lookup_id.delay(time, url)
    print(url)

