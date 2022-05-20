# 用线程池实现多线程爆破
from concurrent.futures import ThreadPoolExecutor
import requests

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
domain = 'baidu.com'


def bengin(sub_name, domain):
    sub_domain = sub_name + '.' + domain
    url = 'http://' + sub_domain
    try:
        response = requests.get(url, headers=headers)
    except:
        # print('{} 子域名不存在！'.format(sub_domain))
        pass
    else:
        if response.status_code == 200:
            print('{} 子域名存在！'.format(sub_domain))


def get_sub():
    with open('../dict/sub_name.txt', 'r') as f:
        while True:
            sub_name = f.readline().strip()
            if not sub_name:
                return
            yield sub_name


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=20) as pool:
        for sub_name in get_sub():
            pool.submit(bengin, sub_name, domain)