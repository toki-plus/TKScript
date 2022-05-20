# 实现从文件中读取子域名
import requests

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}

with open('../dict/sub_name.txt', 'r') as f:
    sub_name = f.readline().strip()
    domain = 'baidu.com'
    while sub_name:
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
        finally:
            sub_name = f.readline().strip()