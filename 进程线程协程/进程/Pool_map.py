from multiprocessing import Pool

import requests
from requests.exceptions import ConnectionError


def scrape(url):
    try:
        print(requests.get(url))
    except ConnectionError:
        print('Error Occured ', url)
    finally:
        print('URL ', url, ' Scraped')


if __name__ == '__main__':
    pool = Pool(processes=3)
    urls = [
        'https://www.baidu.com',
        'http://www.meituan.com/',
        'http://blog.csdn.net/',
        'http://xxxyxxx.net'
    ]
    # map 函数可以遍历每个 URL，然后对其分别执行 scrape 方法
    pool.map(scrape, urls)
