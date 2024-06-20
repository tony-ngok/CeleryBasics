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

    url = f"https://www.themealdb.com/api/json/v1/{key}/{passcode}?i={id}"
    # lookup_id.s(url).apply_async(link=callback) # 回调lookup_id.delay(url)的输出
    # print(url)

    result = lookup_id.delay(url)
    print(url)

    