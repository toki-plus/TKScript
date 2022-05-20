import asyncio
import aiohttp

# 设置请求的最大并发量
CONCURRENCY = 5
URL = 'https://www.baidu.com'

# 创建一个信号量对象，可以用它来控制最大并发量
semaphore = asyncio.Semaphore(CONCURRENCY)
session = None

async def scrape_api():
    # 这里把 semaphore 直接放置在了对应的爬取方法里，使用 async with 语句将 semaphore 作为上下文对象
    # 这样一来，信号量便可以控制进入爬取的最大协程数量 CONCURRNCY
    async with semaphore:
        print('scraping', URL)
        async with session.get(URL) as response:
            await asyncio.sleep(1)
            return await response.text()

async def main():
    global session
    session = aiohttp.ClientSession()
    scrape_index_tasks = [asyncio.ensure_future(scrape_api()) for _ in range(10000)]
    await asyncio.gather(*scrape_index_tasks)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())