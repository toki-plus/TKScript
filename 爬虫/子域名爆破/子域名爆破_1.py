# 实现子域名拼接查询
import requests

sub_name = 'www'
domain = 'baidu.com'
sub_domain = sub_name + '.' + domain
url = 'http://' + sub_domain

# print(url)

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}

try:
    response = requests.get(url, headers=headers)
except:
    print('{} 子域名不存在！'.format(sub_domain))
else:
    if response.status_code == 200:
        print('{} 子域名存在！'.format(sub_domain))