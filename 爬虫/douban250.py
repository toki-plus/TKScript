# 目标：
# 1、爬取站点每一页电影列表，拿到详情页
# 2、提取每部电影的：名称、封面、类别、上映时间、评分、剧情简介
# 3、保存为JSON文件
# 4、使用多线程实现加速

# 实现函数：scrape_page()、scrape_index()、parse_index()、scrape_detail()、parse_detail()、save_data()、main()

import logging
import requests
import re
import json
import multiprocessing
from os import makedirs
from os.path import exists


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

BASE_URL = 'https://movie.douban.com/top250'
TOTAL_PAGES = 10
RESULTS_DIR = 'douban_top_250'
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)


# 请求页面，获得 html
def scrape_page(url):
    logging.info('正在爬取：%s', url)

    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        logging.error('当爬取：%s 时得到无效的状态码：%s', url, response.status_code)
    except requests.RequestException:
        logging.error('当爬取：%s 时发生错误', url, exc_info=True)


# 拼接首页 url，返回该页面的 html
def scrape_index(page):
    index_url = f'{BASE_URL}?start={(page-1)*25}'
    return scrape_page(index_url)


# 解析页面，获取详情页 url
def parse_index(html):
    pattern = re.compile('class="pic".*?href="(.*?)">', re.S)
    items = re.findall(pattern, html)
    if not items:
        return []
    for item in items:
        detail_url = item
        logging.info('获得详情 url：%s', detail_url)
        yield detail_url


# 获取详情页 html 页面
def scrape_detail(url):
    return scrape_page(url)


# 解析详情页
def parse_detail(html):
    name_pattern = re.compile('<span property="v:itemreviewed">(.*?)</span>.*?>(.*?)</span>', re.S)
    name = (re.search(name_pattern, html).group(1).strip()+re.search(name_pattern, html).group(2).strip()) if re.search(name_pattern, html) else None

    return {
        'name': name,
    }


# 保存数据
def save_data(data):
    name = data.get('name')
    data_path = f'{RESULTS_DIR}/{name}.json'
    json.dump(data, open(data_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)


def main(page):
    index_html = scrape_index(page)
    detail_urls = parse_index(index_html)

    for detail_url in detail_urls:
        detail_html = scrape_detail(detail_url)
        data = parse_detail(detail_html)
        logging.info('获取到详情数据：%s', data)
        logging.info('保存数据到json文件')
        save_data(data)
        logging.info('数据已成功保存')


if __name__ == '__main__':
    pool = multiprocessing.Pool()
    pages = [i for i in range(1, TOTAL_PAGES+1)]
    pool.map(main, pages)
    pool.close()
    pool.join()