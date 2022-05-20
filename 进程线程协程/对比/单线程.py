import requests
import time


def task(num):
    url = 'http://www.baidu.com'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
    print('NO.{} waiting for {}'.format(num, url))
    result_code = requests.get(url, headers=headers).status_code
    print('NO.{} get response from {}, Result status code:{}'.format(num, url, result_code))

if __name__ == '__main__':
    start = time.time()

    for num in range(100):
        task(num)

    end = time.time()
    print('Cost time:', end - start) # Cost time: 15.27330207824707