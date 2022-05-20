import requests

response = requests.get('http://192.168.80.132/phpinfo.PHP')
print(response.status_code)