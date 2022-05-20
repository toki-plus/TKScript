import threading
import time


class myThread(threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay

    def run(self):
        print("开始线程：" + self.name)
        # 每个线程执行 3 次
        print_time(self.name, self.delay, 3)
        print("退出线程：" + self.name)


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


# 创建新线程
# 线程 1 每隔 1 秒打印一次时间
thread1 = myThread(1, "Thread-1", 1)
# 线程 2 每隔 2 秒打印一次时间
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()

# 将子线程加入主线程
thread1.join()
thread2.join()

print("退出主线程")

# threading 模块除了包含 _thread 模块中的所有方法外，还提供的其他方法：
# threading.currentThread(): 返回当前的线程变量。
# threading.enumerate(): 返回一个包含正在运行的线程的 list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
# threading.activeCount(): 返回正在运行的线程数量，与 len(threading.enumerate()) 有相同的结果。

# 除了使用方法外，线程模块同样提供了 Thread 类来处理线程，Thread 类提供了以下方法:
# run(): 用以表示线程活动的方法。
# start():启动线程活动。
# join([time]): 等待至线程中止。这阻塞调用线程直至线程的 join() 方法被调用中止、正常退出、抛出未处理的异常 或 可选的超时发生。
# isAlive(): 返回线程是否活动的。
# getName(): 返回线程名。
# setName(): 设置线程名。
