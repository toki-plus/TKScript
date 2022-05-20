import asyncio
from optparse import OptionParser

import aiohttp



async def check_url(request_url):
    global useful_url
    # 这里把 semaphore 直接放置在了对应的爬取方法里，使用 async with 语句将 semaphore 作为上下文对象
    # 这样一来，信号量便可以控制进入爬取的最大协程数量 concurrency
    async with semaphore:
        print(f'checking {request_url}')
        async with session.get(request_url) as response:
            await asyncio.sleep(3)
            if response.status == '200':
                useful_url.append(request_url)
            print('{} status: {}'.format(request_url, response.status))


def get_cmd_args():
    parse = OptionParser()
    parse.add_option('-u', '--url', type='string', dest='url', help='目标url', default='http://192.168.80.132/')
    parse.add_option('-c', '--concurrency', type='int', dest='concurrency', help='并发量', default='100')
    values, args = parse.parse_args()
    url = values.url
    concurrency = values.concurrency
    print("目标url：{}".format(url))
    print("并发量：{}".format(concurrency))
    return url, concurrency


def get_dir_name():
    with open('./php_dir.txt', 'r') as f:
        dir_name = f.readline()
        while dir_name:
            yield dir_name
            dir_name = f.readline()


async def main():
    global session
    async with aiohttp.ClientSession() as session:
        check_tasks = [asyncio.ensure_future(check_url(url+dir_name)) for dir_name in get_dir_name()]
        await asyncio.gather(*check_tasks)


if __name__ == '__main__':
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}

    url, concurrency = get_cmd_args()
    # 创建一个信号量对象，可以用它来控制最大并发量
    semaphore = asyncio.Semaphore(concurrency)
    session = None

    useful_url = []
    print(useful_url)

    asyncio.get_event_loop().run_until_complete(main())

