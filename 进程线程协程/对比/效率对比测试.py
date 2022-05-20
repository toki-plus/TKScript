import requests
import time
import threading
import multiprocessing


# 计算密集型任务
def count(num, lock):
    c = 0
    while c < 500000:
        c += 1
    lock.acquire()
    print('NO.{} result:{}, count over!'.format(num, c))
    lock.release()


# IO密集型任务
def io(num, lock):
    write()
    read()
    lock.acquire()
    print('NO.{} read-write over!'.format(num))
    lock.release()
def write():
        f = open("iotest.txt", "w")
        for x in range(500000):
            f.write("iotest\n")
        f.close()
def read():
    f = open("iotest.txt", "r")
    _ = f.readlines()
    f.close()


# 网络请求密集型任务
def http_request(num, lock):
    url = 'http://www.baidu.com'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
    result_code = requests.get(url, headers=headers).status_code
    lock.acquire()
    print('NO.{} get response from {}, Result status code:{}'.format(num, url, result_code))
    lock.release()


def multi_process(func):
    start = time.time()

    process_lock = multiprocessing.Lock()
    for num in range(100):
        multiprocessing.Process(target=func, args=(num, process_lock)).start()

    end = time.time()
    return end-start


def multi_thread(func):
    start = time.time()

    thread_lock = threading.Lock()
    for num in range(100):
        threading.Thread(target=func, args=(num, thread_lock)).start()

    end = time.time()
    return end-start


if __name__ == '__main__':

    multi_process_count_cost = multi_process(count)
    multi_process_io_cost = multi_process(io)
    multi_process_http_request_cost = multi_process(http_request)

    multi_thread_count_cost = multi_process(count)
    multi_thread_io_cost = multi_process(io)
    multi_thread_http_request_cost = multi_process(http_request)


    print('多进程 ===> 计算密集型耗时：{}\tIO密集型耗时：{}\t网络请求型耗时：{}'.format(multi_process_count_cost, multi_process_io_cost, multi_process_http_request_cost))
    print('多线程 ===> 计算密集型耗时：{}\tIO密集型耗时：{}\t网络请求型耗时：{}'.format(multi_thread_count_cost, multi_thread_io_cost, multi_thread_http_request_cost))
