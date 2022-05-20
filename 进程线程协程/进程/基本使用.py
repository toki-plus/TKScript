import multiprocessing
import time


def process(num):
    time.sleep(num)
    print('Process:', num)


if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=process, args=(i,))
        p.start()

    print('CPU number:' + str(multiprocessing.cpu_count()))
    for p in multiprocessing.active_children():
        print('Child process name: ' + p.name + ' id: ' + str(p.pid))

    print('Process Ended')

# target 表示调用对象，你可以传入方法的名字
# args 表示被调用对象的位置参数元组，比如 target 是函数 a，他有两个参数 m，n，那么 args 就传入 (m, n) 即可
# kwargs 表示调用对象的字典
# name 是别名，相当于给这个进程取一个名字
# group 分组，实际上不使用
