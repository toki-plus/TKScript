import base64
import time

import requests
from lxml import etree

headers = {'cookie': ''}

search_data = '"glassfish" && port="4848" && country="CN"'
search_data_bs64 = str(base64.b64encode(search_data.encode('utf-8')), "utf-8")

for offset in range(1, 11):
    url = 'https://fofa.so/result?page={}qbase64='.format(offset)
    urls = url + search_data_bs64

    try:
        print("正在请求第{}页".format(offset))
        result = requests.get(urls, headers=headers).text

        html = etree.HTML(result)
        etree.tostring(html).decode('utf-8')
        ip_list = html.xpath('//div[@class="re-domain"]/a[@target="_blank"]/@href')
        print(ip_list)

        ip_data = '\n'.join(ip_list)
        with open('fofa_ip.txt', 'w+') as f:
            f.write(ip_data + '\n')
            f.close()

        time.sleep(0.5)
    except:
        pass
