# 实现命令行传参
from concurrent.futures import ThreadPoolExecutor
import requests
from optparse import OptionParser


headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}


def bengin(sub_name, domain):
    sub_domain = sub_name + '.' + domain
    url = 'http://' + sub_domain
    try:
        response = requests.get(url, headers=headers)
    except:
        # print('{} 子域名不存在！'.format(sub_domain))
        pass
    else:
        if response.status_code == 200:
            print('{} 子域名存在！'.format(sub_domain))


def get_sub():
    with open('../dict/sub_name.txt', 'r') as f:
        while True:
            sub_name = f.readline().strip()
            if not sub_name:
                return
            yield sub_name


if __name__ == '__main__':
    parse = OptionParser()
    parse.add_option('-d', '--domain', type='string', dest='domain', help='目标域名', default='baidu.com')
    parse.add_option('-t', '--thread', type='int', dest='thread_num', help='线程数', default='20')

    values, args = parse.parse_args()
    print("传入参数：{}".format(values))
    print("多余参数：{}".format(args))

    # 根据 dest 获取参数
    domain = values.domain
    thread_num = values.thread_num

    print("目标域名：{}".format(domain))
    print("并发量：{}".format(thread_num))

    with ThreadPoolExecutor(max_workers=thread_num) as pool:
        for sub_name in get_sub():
            pool.submit(bengin, sub_name, domain)