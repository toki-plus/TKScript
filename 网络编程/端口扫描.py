import socket
from concurrent.futures import ThreadPoolExecutor
from optparse import OptionParser


def port_scan(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try: sock.connect((host, port))
    except: pass
    else: print('{}:{} | open'.format(host, port))


def get_port(ports):
    port_list = []
    port_list_tmp = ports.split(',')
    for port in port_list_tmp:
        if '-' not in port:
            port_list.append(int(port.strip()))
        else:
            port_span = port.split('-')
            port_start = int(port_span[0].strip())
            port_end = int(port_span[1].strip())
            for port in range(port_start, port_end + 1):
                port_list.append(port)
    # for port in port_list:
    #     yield port
    return port_list

def cmd_get_params():
    parse = OptionParser('%prog -d 域名 -p 端口 -t 线程数\n'
                         '示例（默认）：%prog -d www.baidu.com -p 21-23,25,53,67-68,80-443,110,139,143,161,389,445,512-514,873,1080,1352,1433,1521,2049,2181,2375,3306,3389,4848,5000,5432,5632,5900,6379,7001-7002,8069,8161,8080-8089,8083-8086,9000,9090,9200-9300,11211,27017-27018 -t 100\n'
                         '注意：线程数不能大于所给的端口个数')
    parse.add_option('-d', '--domain', type='string', dest='domain', help='目标域名', default='www.baidu.com')
    parse.add_option('-p', '--port', type='string', dest='ports', help='端口号', default='21-23,25,53,67-68,80-443,110,139,143,161,389,445,512-514,873,1080,1352,1433,1521,2049,2181,2375,3306,3389,4848,5000,5432,5632,5900,6379,7001-7002,8069,8161,8080-8089,8083-8086,9000,9090,9200-9300,11211,27017-27018')
    parse.add_option('-t', '--thread', type='int', dest='thread_num', help='线程数', default='100')

    values, _ = parse.parse_args()
    print("传入参数：{}".format(values))
    # 根据 dest 获取参数
    domain = values.domain
    ports = values.ports
    thread_num = values.thread_num

    print("目标域名：[{}]".format(domain))
    print("目标端口号：[{}]".format(ports))
    print("并发量：[{}]".format(thread_num))

    return domain, ports, thread_num

if __name__ == '__main__':
    domain, ports, thread_num = cmd_get_params()

    with ThreadPoolExecutor(max_workers=thread_num) as executor:
        for port in get_port(ports):
            executor.submit(port_scan, domain, port)


# 打包：pyinstaller -F -i favicon.ico 端口扫描.py