import socket
import os
import whois
import time
import nmap

# 域名反查 IP
# real_ip = socket.gethostbyname('baidu.com')
# print(real_ip)

# nslookup 识别 CDN，根据返回的 Address 的个数来判断
# nslookup_obj = os.popen('nslookup baidu.com')
# cdn_result = nslookup_obj.read()
# print(cdn_result)
# # 可以用正则表达式判断 IP 出现的个数
# # 用点的个数来判断 IP 的个数
# if cdn_result.count('.') > 10:
#     print("CDN 存在")
# else:
#     print('CDN 不存在')

# 端口扫描
# socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# result = socket.connect_ex(('www.baidu.com', 80))
# if result == 0:
#     print('open')
# else:
#     print('close')

# whois 查询，使用 python-whois 包
# result = whois.whois('baidu.com')
# print(result)

# 子域名查询
# for sub in open('子域名字典.txt'):
#     sub = sub.replace('\n', '')
#     url = sub + '.xueersi.com'
#     try:
#         ip = socket.gethostbyname(url)
#         print(url + '->' + ip)
#         time.sleep(0.1)
#     except Exception:
#         pass

# nmap 端口扫描
nm = nmap.PortScanner()
data = nm.scan('www.xiaodi8.com', '80,443', '-sV')
print(data)
