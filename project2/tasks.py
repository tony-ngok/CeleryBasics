# 网路请求任务

from celery_app import app
from requests import get, exceptions
from celery.exceptions import Ignore, MaxRetriesExceededError
from celery.signals import task_success

@app.task(bind=True, max_retries=2, default_retry_delay=5)
def lookup_id(self, url):
    try:
        try:
            resp = get(url, timeout=5)
            resp.raise_for_status()
            print(f"Code: {resp.status_code}")

            data = resp.json()
            return data
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
            raise Ignore()
        
        # https://stackoverflow.com/questions/67968018/how-to-execute-some-code-at-last-retry-of-a-celery-task
        except exceptions.ConnectionError:
            print("RETRY: connexion...")
            raise self.retry()

    except MaxRetriesExceededError as mre_err:
            print("FAIL: can't retry more")
            self.update_state('FAILURE', meta={
            'exc_type': type(mre_err).__name__,
            'exc_message': 'Maximum retries exceeded'
            })
    raise Ignore()

