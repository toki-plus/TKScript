import time
from multiprocessing import Pool, Process


def function(index):
    print('{} 执行了第 {} 个进程'.format(index))
    time.sleep(1)


if __name__ == '__main__':
    pool = Pool(processes=8)

    # 用 8 个进程执行 30 次函数
    for i in range(100):
        pool.apply_async(function, (i,))

    pool.close()
    pool.join()
