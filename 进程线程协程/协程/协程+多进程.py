import asyncio
import time

import aiohttp
from aiomultiprocess import Pool

start = time.time()


async def get(url):
    session = aiohttp.ClientSession()
    response = await session.get(url)
    result = await response.text()
    session.close()
    return result


async def request():
    url = 'http://www.baidu.com'
    urls = [url for _ in range(100)]
    async with Pool() as pool:
        result = await pool.map(get, urls)
        return result

if __name__ == '__main__':

    task = asyncio.ensure_future(request())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(task)

    end = time.time()
    print('Cost time:', end - start)
