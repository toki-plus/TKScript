import threading
import time
from concurrent.futures import ThreadPoolExecutor


def task(i):
    print('第 {} 次由子线程 {} 打印'.format(i, threading.current_thread().name))
    time.sleep(1)


if __name__ == '__main__':
    start = time.time()
    print('主线程名：{}'.format(threading.current_thread().name))
    with ThreadPoolExecutor(max_workers=10) as pool:
        # 用 10 个线程打印 30 次
        for i in range(30):
            pool.submit(task, i)
    end = time.time()
    print('用时：{}'.format(end - start))
