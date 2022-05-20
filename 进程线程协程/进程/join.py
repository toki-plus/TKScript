import time
from multiprocessing import Process


class MyProcess(Process):
    def __init__(self, loop):
        Process.__init__(self)
        self.loop = loop

    def run(self):
        for count in range(self.loop):
            time.sleep(1)
            print('Pid: ' + str(self.pid) + ' LoopCount: ' + str(count))


if __name__ == '__main__':
    # 启动 3 个进程，第一个进程执行 2 次，第二个进程执行 3 次，第三个进程执行 4 次
    for i in range(2, 5):
        p = MyProcess(i)
        # 子进程随着主进程的结束而结束
        p.daemon = True
        p.start()
        # 将子进程加入主进程
        p.join()

    print('Main process Ended!')
