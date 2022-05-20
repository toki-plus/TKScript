import time
from multiprocessing import Process, Semaphore, Lock, Queue

# 定义了一个共享队列，利用了 Queue 数据结构
buffer = Queue(10)
# 信号量，代表缓冲区空余数
empty = Semaphore(2)
# 信号量，代表缓冲区占用数
full = Semaphore(0)
lock = Lock()


# 消费者
class Consumer(Process):
    def run(self):
        global buffer, empty, full, lock
        while True:
            # 占用一个缓冲区位置
            # 缓冲区占用数 - 1
            # 缓冲区空余数 + 1
            full.acquire()
            lock.acquire()
            # 队列 - 1
            buffer.get()
            print('Consumer pop an element')
            time.sleep(1)
            lock.release()
            empty.release()


# 生产者
class Producer(Process):
    def run(self):
        global buffer, empty, full, lock
        while True:
            # 占用一个缓冲区位置
            # 缓冲区空余数 - 1
            # 缓冲区占用数 + 1
            empty.acquire()
            # 加锁
            lock.acquire()
            # 队列 + 1
            buffer.put(1)
            print('Producer append an element')
            time.sleep(1)
            # 解锁
            lock.release()
            full.release()


if __name__ == '__main__':
    p = Producer()
    c = Consumer()
    p.daemon = c.daemon = True
    p.start()
    c.start()
    p.join()
    c.join()
    print('Ended!')
