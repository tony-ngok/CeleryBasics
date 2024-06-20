# 网路请求任务

from celery_app import app
from requests import get, exceptions
from celery.exceptions import Ignore, MaxRetriesExceededError, SoftTimeLimitExceeded
from time import sleep

@app.task(bind=True, max_retries=2, default_retry_delay=5, soft_time_limit=20)
def lookup_id(self, key, passcode, id, sleep_time):
    url = f"https://www.themealdb.com/api/json/v1/{key}/{passcode}?i={id}"

    try:
        sleep(sleep_time)

        try:
            resp = get(url, timeout=5)
            resp.raise_for_status()
            print(f"Code: {resp.status_code}")

            data = resp.json()
            return data
        
        # 如果HTTP有问题就放弃
        except exceptions.HTTPError as http_err:
            if resp.status_code == 403:
                print("FAIL: URL verboten")
            elif resp.status_code == 404:
                print("FAIL: URL not found")
            else:
                print("FAIL: unknown URL error")
            
            self.update_state('FAILURE', meta={
                'exc_type': type(http_err).__name__,
                'exc_message': 'HTTP error'
                })
            raise Ignore() # 不再管这个任务了
        
        # https://stackoverflow.com/questions/67968018/how-to-execute-some-code-at-last-retry-of-a-celery-task
        # 如果网路连结有问题就重试
        except exceptions.ConnectionError:
            print("RETRY: connexion...")
            raise self.retry()

    # 重试超过2次就直接放弃
    except MaxRetriesExceededError as mre_err:
        print("FAIL: can't retry more")
        self.update_state('FAILURE', meta={
            'exc_type': type(mre_err).__name__,
            'exc_message': "Can't retry more"
            })
        raise Ignore()

    # 如果任务超时就算作失败
    except SoftTimeLimitExceeded as to_err:
        print("FAIL: timeout")
        self.update_state('FAILURE', meta={
            'exc_type': type(to_err).__name__,
            'exc_message': 'Timeout'
            })
        raise Ignore()