import _thread
import time


# 为线程定义一个函数
def print_time(threadName, delay):
    count = 0
    # 每个线程打印 3 次
    while count < 3:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())))


# 创建两个线程
try:
    # 线程 1 每隔 2 秒打印一次时间
    _thread.start_new_thread(print_time, ("Thread-1", 2,))
    # 线程 2 每隔 4 秒打印一次时间
    _thread.start_new_thread(print_time, ("Thread-2", 4,))
except:
    print("Error: 无法启动线程")

while 1:
    pass
