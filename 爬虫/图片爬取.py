import json
import logging
import os
import re
import time
from concurrent.futures import ThreadPoolExecutor

import requests

if not os.path.exists('images'):
    os.mkdir(os.getcwd() + '/images')

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
base_url = 'https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start={}'
url_list = [base_url.format(offest) for offest in range(0, 101, 20)]


def get_urls():
    imgs_urlss = []
    for url in url_list:
        response = requests.get(url, headers=headers)
        data = json.dumps(response.json())
        pattern = re.compile('"cover": "(.*?)",', re.S)
        imgs_urls = re.findall(pattern, data)
        imgs_urlss.extend(imgs_urls)
    return imgs_urlss


def download_img(img_url):
    response = requests.get(img_url)
    img_data = response.content
    img_name = img_url.split('/')[-1]

    with open('images/' + img_name, 'wb') as f:
        f.write(img_data)

    logging.info(img_name + '下载成功！')


if __name__ == '__main__':
    start_time = time.time()

    img_urls = get_urls()
    with ThreadPoolExecutor(max_workers=10) as pool:
        for img_url in img_urls:
            pool.submit(download_img, img_url)

    end_time = time.time()
    print("time cost: {}".format(end_time - start_time))
