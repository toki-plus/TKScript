from scapy.all import *
from concurrent.futures import ThreadPoolExecutor
from optparse import OptionParser

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


def host_scan(dst_ip, delay):
    pkt = IP()/ICMP()/'hello'
    pkt[IP].dst = dst_ip
    res = sr1(pkt, timeout=delay, verbose=False)
    if(res):
        print('✅ {} 在线'.format(res[IP].src))
    else:
        print('❎ {} 离线'.format(dst_ip))


def get_ip(dst_ip):
    # 192.168.80.1-254
    if '-' not in dst_ip:
        return dst_ip
    else:
        index = dst_ip.rfind('.')
        ip_prefix = dst_ip[:index+1]

        ip_suffix_span = dst_ip.split('.')[-1].split('-')
        ip_suffix_start = int(ip_suffix_span[0])
        ip_suffix = int(ip_suffix_span[-1])
        for ip_suffix in range(ip_suffix_start, ip_suffix+1):
            dst_ip = ip_prefix + str(ip_suffix)
            yield dst_ip


def cmd_get_params():
    parse = OptionParser('%prog -d 目标网段 -t 线程数\n'
                         '示例（默认）：%prog -d 192.168.80.1-254 -t 100 -d 1\n')
    parse.add_option('-i', '--ip', type='string', dest='dst_ip', help='目标网段', default='192.168.80.1-254')
    parse.add_option('-t', '--thread', type='int', dest='thread_num', help='线程数', default='100')
    parse.add_option('-d', '--delay', type='int', dest='delay', help='延迟时间', default='1')

    values, _ = parse.parse_args()
    print("传入参数：{}".format(values))

    dst_ip = values.dst_ip
    thread_num = values.thread_num
    delay = values.delay

    print("目标网段：[{}]".format(dst_ip))
    print("并发量：[{}]".format(thread_num))
    print("延迟时间：[{}]".format(delay))

    return dst_ip, thread_num, delay


if __name__ == '__main__':

    dst_ip, thread_num, delay = cmd_get_params()

    with ThreadPoolExecutor(max_workers=thread_num) as executor:
        for dst_ip in get_ip(dst_ip):
            executor.submit(host_scan, dst_ip, delay)

# 打包：pyinstaller -F -i favicon.ico 端口扫描.py