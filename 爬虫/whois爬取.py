import requests
import re
import os
from parsel import Selector

if not os.path.exists('result'):
    os.mkdir(os.getcwd() + '/result')

url = 'https://www.whois.com/whois/baidu.com'

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}

response = requests.get(url, headers=headers)

# print(response.text)

selector = Selector(text=response.text)
data = selector.css('.whois-data').get()

pattern = re.compile('df-label">(.*?)<.*?df-value">(.*?)<', re.S)
data = re.findall(pattern,data)

print(data)

with open('result/whois_info.txt', 'w') as f:
    for k, v in data:
        f.write('{} {}\n'.format(k, v))
